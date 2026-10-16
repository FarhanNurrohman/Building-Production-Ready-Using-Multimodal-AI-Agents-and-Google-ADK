# 🚀 Building Production-Ready Using Multimodal AI Agents and Google ADK

Official repository and workshop material for **DevFest Cloud Surabaya**. This project demonstrates how to build, test, and deploy a production-grade multimodal AI agent leveraging the modern **Google GenAI ADK (Agent Development Kit)**, **Flask**, and **Streamlit**, containerized for **Google Cloud Run**.

---

## 📂 Project Structure

Based on your workspace organization, the project follows this clean architecture:

```text
gdg-devfest-surabaya/
│
├── .venv/                  # Python Virtual Environment
├── script/                 
│   └── genAI.py            # Flask Backend API (Google ADK & Multimodal Engine)
├── .env                    # Environment variables (API Keys)
├── app.py                  # Streamlit Frontend UI
├── requirements.txt        # Project dependencies
└── readme.md               # Documentation
```

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (Interactive 2-column dashboard)
* **Backend:** [Flask](https://flask.palletsprojects.com/) (REST API & Hybrid Payload Handler)
* **AI Engine:** [Google GenAI SDK / ADK](https://github.com/google/genai-python) (`gemini-2.5-flash`)
* **Cloud & DevOps:** Docker & Google Cloud Run

---

## ⚙️ Getting Started & Installation

### 1. Clone or Setup Workspace
Ensure your project folder matches the structure above. Open your terminal in the root directory.

### 2. Create and Activate Virtual Environment
```bash
python -m venv .venv
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate
```

### 3. Install Dependencies
Create or use your `requirements.txt` containing:
```text
flask
streamlit
requests
google-genai
python-dotenv
pandas
```
Install them via pip:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory and add your personal Google Gemini API Key:
```env
GEMINI_API_KEY=your_actual_gemini_api_key_here
```

---

## 🚀 Running the Application Locally

To test the system locally, you need to run both the Flask backend and the Streamlit frontend in **two separate terminal windows**.

### Terminal 1: Run Flask Backend
Navigate into your script folder and start the server:
```bash
cd script
python genAI.py
```
*The server will run on `http://127.0.0.1:5000`.*

### Terminal 2: Run Streamlit Frontend
From the root directory, launch the Streamlit app:
```bash
streamlit run app.py
```
*The web interface will automatically open in your browser at `http://localhost:8501`.*

---

## ☁️ Deployment to Google Cloud Run (Pemateri Demo)

To containerize and push the backend service to GCP Cloud Run:

1. **Build Docker Image:**
   ```bash
   docker build -t gcr.io/your-gcp-project-id/multimodal-agent-backend:latest .
   ```
2. **Push to Container Registry / Artifact Registry:**
   ```bash
   docker push gcr.io/your-gcp-project-id/multimodal-agent-backend:latest
   ```
3. **Deploy to Cloud Run:**
   ```bash
   gcloud run deploy multimodal-agent-backend \
     --image gcr.io/your-gcp-project-id/multimodal-agent-backend:latest \
     --platform managed \
     --region asia-southeast2 \
     --allow-unauthenticated \
     --set-env-vars GEMINI_API_KEY=your_api_key
   ```

---

## 📝 Workshop Agenda (90 Minutes)

1. **Part 1: Fondasi AI Agent & Kapabilitas Google ADK (15 Min)** – Understanding the agentic paradigm, stateless vs stateful workflows, and native multimodal engineering.
2. **Part 2: Live Coding - Core Agent with Flask & Google ADK (35 Min)** – Writing backend logic, handling hybrid payloads (`request.form` & `request.files`), and configuring model parameters (`temperature`, `System Instructions`).
3. **Part 3: Integration, Stateful Session, & Local Testing (15 Min)** – Connecting Streamlit UI with the local Flask server and running end-to-end multimodal tests.
4. **Part 4: Cloud Architecture & Deployment to Google Cloud Run (25 Min)** – Live containerization demo and public deployment on GCP.

---
*Created with ❤️ for DevFest Cloud Surabaya.*