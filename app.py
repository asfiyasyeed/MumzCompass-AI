import json
import os
from dotenv import load_dotenv
from openai import OpenAI

# 1. Load the secret API Key from .env
load_dotenv()
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENROUTER_API_KEY"),
)

# 2. Function to load  Knowledge Base
def load_knowledge_base():
    with open("knowledge_base.json", "r", encoding="utf-8") as f:
        return json.load(f)

kb_data = load_knowledge_base()

def analyze_mother_input(user_message):
    # This prompt tells the AI exactly how to behave (Safety + Accuracy)
    system_prompt = f"""
    You are a Mumzworld Pediatric Assistant. 
    Analyze the mother's message using this Knowledge Base: {json.dumps(kb_data['milestones'])}
    
    RULES:
    1. Identify the child's age/milestone.
    2. If the message mentions medical danger (fever, bleeding, etc.), set 'medical_emergency' to true.
    3. Return ONLY a JSON object with: 
       - 'selected_milestone_index': (0-6)
       - 'medical_emergency': (true/false)
       - 'explanation_en': (short encouraging text)
       - 'explanation_ar': (natural Arabic translation)
    """

    response = client.chat.completions.create(
        model="openai/gpt-4o-mini", # Using the most reliable free endpoint
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message}
        ],
        response_format={ "type": "json_object" } 
    )
    
    # --- THIS IS THE NEW CLEANING LOGIC ---
    content = response.choices[0].message.content
    
    # This ensures that even if the AI adds "Here is your JSON:", we only get the { } part
    if "```json" in content:
        content = content.split("```json")[1].split("```")[0].strip()
    elif "{" in content:
         content = content[content.find("{"):content.rfind("}")+1]
         
    return json.loads(content)

def get_recommendations(analysis_results):
    idx = analysis_results['selected_milestone_index']
    # Safety Check: Return medical warning if emergency detected
    if analysis_results['medical_emergency']:
        return "Please contact a doctor immediately.", []
    
    # Get the products from your JSON
    recommended_products = kb_data['milestones'][idx]['products']
    return analysis_results, recommended_products



import streamlit as st

# Set Page Config
st.set_page_config(page_title="Mumzworld AI Companion", page_icon="🤱", layout="centered")

# --- UI Header ---
st.title("🤱 Mumzworld AI Companion")
st.markdown("### *Personalized guidance for your motherhood journey*")
st.divider()

# --- Language Selection ---
lang = st.radio("Select Language / اختر اللغة", ["English", "العربية"], horizontal=True)

# --- Input Area ---
user_input = st.text_area(
    "How can we help you and your little one today?" if lang == "English" else "كيف يمكننا مساعدتك وطفلك اليوم؟",
    placeholder="e.g., My 7 month old just started crawling..." if lang == "English" else "مثلاً: طفلي عمره 7 أشهر وقد بدأ في الحبو..."
)

if st.button("Get Guidance" if lang == "English" else "احصل على التوجيه"):
    if user_input:
        with st.spinner("Thinking..." if lang == "English" else "جاري التفكير..."):
            try:
                # 1. Get Analysis
                analysis = analyze_mother_input(user_input)
                
                # 2. Check for Medical Emergency First!
                if analysis.get('medical_emergency'):
                    st.error("⚠️ EMERGENCY NOTICE / تنبيه طوارئ")
                    st.write("Please contact your pediatrician immediately. / يرجى الاتصال بطبيب الأطفال فوراً.")
                else:
                    # 3. Display Guidance
                    st.success("Developmental Insight / نظرة تطويرية")
                    st.write(analysis['explanation_en'] if lang == "English" else analysis['explanation_ar'])
                    
                    st.divider()
                    
                    # 4. Display Curated Products
                    st.subheader("Curated Essentials / أساسيات مختارة")
                    idx = analysis['selected_milestone_index']
                    products = kb_data['milestones'][idx]['products']
                    
                    cols = st.columns(len(products))
                    for i, p in enumerate(products):
                        with cols[i]:
                            st.info(f"**{p['name']}**")
                            st.caption(f"Category: {p['category']}")
                            st.write(p['reason_en'] if lang == "English" else p['reason_ar'])
                            
            except Exception as e:
                st.error(f"Error: {e}")
    else:
        st.warning("Please enter a message first.")