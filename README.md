# MumzCompass-AI
🤱 MumzCompass AI: The Developmental Co-Pilot
Mumzworld AI-Native Intern Assessment | Track A: AI Engineering

🌟 The Problem
Independent mothers often feel overwhelmed by generic blogs and massive e-commerce catalogs. They don't need more products; they need contextual guidance at 2 AM when they are observing a new behavior in their child.

🚀 The Solution
MumzCompass is a multilingual AI agent that bridges the gap between pediatric milestones and e-commerce. Instead of searching for "High Chairs," a mother simply describes her baby's progress (e.g., "My 6-month-old is finally sitting up!"). The agent:

Analyzes the developmental stage using a grounded Knowledge Base.

Educates the mother on what to expect next (English & Arabic).

Curates specific essentials that match that exact developmental "signal."

Protects by triggering safety guardrails if medical symptoms are detected.

🛠️ The Tech Stack
Language: Python 3.x

AI Engine: OpenAI gpt-4o-mini (via OpenRouter)

Interface: Streamlit (For a production-ready web feel)

Data Strategy: Grounded JSON Knowledge Base (RAG-inspired architecture)

🏗️ Architecture & Trade-offs
Why a Grounded Knowledge Base?
I deliberately chose to use a local knowledge_base.json rather than letting the AI answer freely. This ensures:

Zero Hallucinations: The agent only recommends products actually in the Mumzworld-style catalog.

Safety First: I implemented a specific "Medical Deferral" logic. If a user mentions a fever or injury, the agent prioritizes a doctor's visit over a product sale.

The Pivot (Technical Troubleshooting):
During development, I encountered 404/400 errors with several free-tier Llama and Gemini models on OpenRouter. I successfully pivoted to gpt-4o-mini, proving system resilience and the ability to troubleshoot API instability under pressure.

🚦 Setup & Installation (Under 2 Minutes)
Clone the Repo:
git clone [Your-Repo-Link]

Create Virtual Environment:
python -m venv venv
source venv/bin/activate (or .\venv\Scripts\activate on Windows)

Install Dependencies:
pip install -r requirements.txt

Add API Key:
Create a .env file and add: OPENROUTER_API_KEY=your_key_here

Run the App:
streamlit run app.py

📊 Evaluation
See EVALS.md for a detailed breakdown of 10 stress tests, including:

Bilingual (English/Arabic) mixed input handling.

Behavior-based age inference.

Safety guardrail triggers for medical emergencies.

🤖 Tooling Transparency
Cursor/VS Code: Primary IDE for development.

AI Assistance: Used for structuring the Streamlit layout and debugging OpenRouter model ID mismatches.

Loom: Used for the final walkthrough demonstration.


🗺️ Future Roadmap: Scaling MumzCompass
If given additional development time, I would focus on transforming this prototype into a full-scale production system:

Dynamic RAG with Vector Databases: Transition from a static JSON knowledge base to a Vector Database (like Pinecone or FAISS). This would allow the agent to perform Retrieval-Augmented Generation (RAG) over thousands of real Mumzworld product descriptions and blog articles, providing even deeper context.

Voice-to-Guidance (Arabic/English): Integrating Whisper (STT) to allow busy mothers to record a voice note while multi-tasking. The AI would process the audio, identify the milestone, and respond with a summarized voice note using ElevenLabs.

Predictive Timeline Personalization: Using historical interaction data to predict the next developmental leap. For example, if a mother mentions her baby is "rolling" today, the app would automatically suggest "crawling-safety" tips and products in exactly two months.

Computer Vision Integration: A feature where a mother can upload a photo of a diaper rash or a product label, and the AI uses Vision Models to categorize the concern or explain product usage in her native language.
