# 🤱 MumzCompass AI: The Developmental Co-Pilot

**Mumzworld AI-Native Intern Assessment | Track A: AI Engineering**

---

## 🌟 The Problem

Independent mothers often feel overwhelmed by generic blogs and massive e-commerce catalogs. They don't need more products—they need **contextual, real-time guidance**, especially during uncertain moments (like 2 AM when a new behavior appears).

---

## 🚀 The Solution

**MumzCompass** is a multilingual AI agent that bridges the gap between **developmental science** and **e-commerce guidance**.

Instead of searching for products like *"High Chairs"*, a mother simply describes her baby’s behavior:

> *"My 6-month-old is finally sitting up!"*

The AI agent then:

- 🧠 **Analyzes** the developmental stage using a grounded Knowledge Base  
- 📚 **Educates** the mother on what to expect next (English & Arabic)  
- 🛍️ **Recommends** relevant products tied to that exact milestone  
- 🚨 **Protects** by triggering safety guardrails if medical symptoms are detected  

---

## 🛠️ Tech Stack

- **Language:** Python 3.x  
- **AI Engine:** OpenAI `gpt-4o-mini` (via OpenRouter)  
- **Interface:** Streamlit (production-style UI)  
- **Data Strategy:** Grounded JSON Knowledge Base (RAG-inspired architecture)  

---

## 🏗️ Architecture & Trade-offs

### 🔹 Why a Grounded Knowledge Base?

Instead of allowing free-form AI responses, the system uses a structured local dataset (`knowledge_base.json`).

This ensures:

- ❌ **Zero Hallucinations**  
  Only predefined, relevant products are recommended  

- 🛡️ **Safety First**  
  A built-in **Medical Deferral System** overrides all logic if symptoms like:
  - fever  
  - pain  
  - injury  
  are detected  

  → The user is immediately advised to consult a pediatrician  

---

### 🔄 The Pivot (Technical Resilience)

During development, multiple OpenRouter models (Llama, Gemini) returned **404 / 400 errors**.

Instead of blocking progress:
- Switched to **`gpt-4o-mini`**
- Stabilized API behavior
- Ensured consistent performance

This demonstrates **real-world debugging and adaptability under constraints**.

---

## 🚦 Setup & Installation (Under 2 Minutes)

### 1. Clone the Repository

git clone https://github.com/asfiyasyeed/MumzCompass-AI
cd MumzCompass-AI

## 2. Create Virtual Environment
python -m venv venv  
source venv/bin/activate      # Mac/Linux  
.\venv\Scripts\activate       # Windows  

## 3. Install Dependencies
pip install -r requirements.txt  

## 4. Add API Key

Create a .env file:

OPENROUTER_API_KEY=your_key_here  

## 5. Run the App
streamlit run app.py  

---

## 📊 Evaluation & Testing
To ensure the system is production-ready, I performed rigorous testing across 10 distinct scenarios, covering:

Safety: 100% success rate in triggering medical deferral logic.

Multilingual: Flawless handling of mixed English/Arabic inputs.

Accuracy: Zero product hallucinations due to the grounded Knowledge Base.

Note: For the full breakdown of test cases, inputs, and expected vs. actual outputs, please see the EVALS.md file. 

---

## 🤖 Tooling Transparency

- Cursor / VS Code: Primary development environment  
- AI Assistance:  
  - Streamlit UI structuring  
  - Debugging OpenRouter integration issues  
- Loom: Used for final walkthrough demo  

---

## 🗺️ Future Roadmap: Scaling MumzCompass

With more development time, this prototype can evolve into a full production system:

### 🔹 1. Dynamic RAG with Vector Database

- Move from static JSON → Vector DB (FAISS / Pinecone)  
- Enable semantic search across:  
  - real product catalogs  
  - parenting articles  
- Provide deeper, contextual recommendations  

### 🔹 2. Voice-to-Guidance (Arabic + English)

- Integrate Whisper (Speech-to-Text)  
- Allow mothers to send voice notes  
- Respond with AI-generated voice (e.g., ElevenLabs)  

### 🔹 3. Predictive Development Timeline

- Track user interactions  
- Predict upcoming milestones  

Example:

If baby is "rolling" → suggest "crawling safety" in ~2 months  

### 🔹 4. Computer Vision Integration

Upload:  
- product labels  
- baby conditions (non-critical)  

Use Vision Models to:  
- explain usage  
- categorize concerns  
- respond in native language  
