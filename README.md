📊 Trade Opportunities Analyzer

A full-stack application that analyzes Indian market sectors and generates structured trade opportunity reports using AI.

🚀 Project Overview

This project consists of:

🔹 Backend (FastAPI) → Generates AI-powered markdown reports

🔹 Frontend (React) → Simple UI to request analysis and download reports

The system accepts a sector name (e.g., technology, pharmaceuticals) and returns a downloadable markdown report.

🏗️ Tech Stack
Backend:

FastAPI

Google Gemini (google-genai)

DuckDuckGo Search

JWT Authentication

SlowAPI (Rate Limiting)

Frontend:

React (Vite)

Axios

📁 Project Structure

backend/
├── app/
│ ├── main.py
│ ├── routes/
│ │ └── analyze.py
│ ├── services/
│ │ ├── scraper.py
│ │ ├── ai_service.py
│ │ └── report.py
│ ├── core/
│ │ ├── config.py
│ │ ├── security.py
│ │ ├── rate_limiter.py
│ │ └── session_store.py
│ └── utils/
│ └── logger.py
├── requirements.txt
├── generate_token.py
└── .env

frontend/
├── src/
│ ├── App.jsx
│ ├── api.js
│ └── components/
│ └── Analyzer.jsx
├── package.json

⚙️ Backend Setup
1. Navigate to backend

cd backend

2. Create Virtual Environment

python -m venv venv
source venv/bin/activate # Windows: venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt

4. Create .env

GEMINI_API_KEY=your_gemini_api_key
SECRET_KEY=your_random_secret_key
RATE_LIMIT=5/minute

5. Run Backend

uvicorn app.main --reload

Backend runs at:
http://127.0.0.1:8000

🔐 Authentication

Generate JWT token:

python generate_token.py

Use in requests:

Authorization: Bearer <your_token>

📡 API Endpoint

GET /analyze/{sector}

Example:

GET /analyze/technology

📄 Response

Returns markdown content

Automatically downloads as:

technology_report.md

🎨 Frontend Setup
1. Navigate to frontend

cd frontend

2. Install Dependencies

npm install

3. Run Frontend

npm run dev

Frontend runs at:
http://localhost:5173

🌐 Frontend Usage

Enter sector name

Enter JWT token

Click Analyze

Markdown report downloads automatically

🔒 Security Features

JWT Authentication

Input validation

Rate limiting (per user)

Session tracking

CORS protection

Logging & error handling

⚠️ Authentication Note

To comply with the single endpoint requirement, JWT tokens are generated manually.

In production, this would be replaced with:

Login system

Secure token storage

Refresh tokens

☁️ Deployment
Backend:

Render / Railway

Frontend:

Vercel

🔗 Deployment Links

Frontend: https://trade-opportunities-analyzer.vercel.app
Backend: https://trade-opportunities-analyzer.onrender.com

✅ Features

AI-powered market analysis

Real-time data scraping

Structured markdown reports

Downloadable .md files

Secure API with rate limiting

Clean architecture
