I Predictor (XGBoost + SHAP)	Predicts best-fit careers and visualizes feature importance with SHAP explainability.
💬 LLM Career Coach	Generates personalized career roadmaps and motivational guidance using LLM reasoning.
⚙️ FastAPI Backend	Serves AI predictions, roadmaps, SHAP data, and animation cues via JSON API.
💻 React Frontend	Stunning animated UI built with TailwindCSS, Framer Motion, GSAP, and Lottie.
🎨 3D & Animation Engine	Engages users with cinematic transitions, Lottie animations, and Three.js 3D visualizations.
🐳 Dockerized Deployment	Fully containerized stack for easy setup and deployment.
💾 MongoDB Database	Stores user feedback, reports, and analytics data.
🧠 System Architecture
LifePathAI/
├── backend/
│   ├── main.py
│   ├── models/
│   ├── routes/
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── pages/
│   │   │   ├── Home.jsx
│   │   │   ├── Form.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── Roadmap.jsx
│   │   │   └── Report.jsx
│   │   ├── components/
│   │   │   ├── AnimatedButton.jsx
│   │   │   ├── PredictionChart.jsx
│   │   │   ├── SHAP3D.jsx
│   │   │   ├── RoadmapTimeline.jsx
│   │   │   ├── LottiePlayer.jsx
│   │   │   └── Loader.jsx
│   │   ├── assets/
│   │   │   ├── ai_brain.json
│   │   │   ├── data_flow.json
│   │   │   ├── growth_curve.json
│   │   │   └── report_done.json
│   │   └── styles/
│   │       └── animations.css
│   └── package.json
│
├── docker-compose.yml
├── Dockerfile
├── README.md
└── LICENSE

🚀 Tech Stack
🧩 Frontend

React 18

TailwindCSS

Framer Motion

GSAP + ScrollTrigger

LottieFiles / react-lottie-player

Three.js / react-three-fiber

⚙️ Backend

FastAPI

XGBoost, SHAP

OpenAI / LLM APIs

Pydantic, CORS

💾 Database

MongoDB Atlas

🐳 DevOps

Docker + Docker Compose

Nginx reverse proxy (optional for production)

🌈 User Experience Flow
Page	Animation Type	Tools
🏠 Home Page	Floating icons + gradient shift	GSAP, Framer Motion
📝 Form Page	Step-by-step field reveal	Framer Motion
📊 Dashboard	Animated probability bars + SHAP bubbles	Chart.js + Framer Motion
🌟 Roadmap	Scroll-triggered AI roadmap timeline	GSAP ScrollTrigger
🧾 Report Page	AI generating report (Lottie)	LottieFiles
🧩 API Endpoints
Route	Method	Description
/predict	POST	Returns top career predictions, SHAP summary, and animation theme
/report	GET	Generates and returns downloadable PDF report
/feedback	POST	Stores user feedback
/health	GET	Health check endpoint

Example response:

{
  "top_careers": [
    {"career": "AI Engineer", "prob": 0.82},
    {"career": "Data Analyst", "prob": 0.11},
    {"career": "Software Engineer", "prob": 0.07}
  ],
  "shap_summary": [
    {"feature": "analytical_index", "contribution": 0.21}
  ],
  "llm_response": {
    "summary": "You have strong analytical and logical reasoning abilities..."
  },
  "animation_theme": "growth_curve",
  "animation_mood": "optimistic_rise"
}

⚙️ Installation & Setup
🐳 Option 1: Run with Docker
git clone https://github.com/<your-username>/LifePathAI.git
cd LifePathAI
docker-compose up --build


Access the app at 👉 http://localhost:3000

💻 Option 2: Manual Setup

Backend

cd backend
pip install -r requirements.txt
uvicorn main:app --reload


Frontend

cd frontend
npm install
npm run dev

🧾 Demo Instructions (for video)

Start with animated landing page intro

Fill in the student’s academic and skill form

Watch animated AI “data flow” Lottie

Dashboard reveals career predictions with bars & bubbles

Scroll roadmap timeline

Generate & download report (animated loader)

📸 Screenshots / Preview

(Add screenshots or GIFs here once deployed)
Example placeholders:

🏠 Home Page

📝 Input Form

📊 Dashboard Visualization

🌟 3D Career Path

🧾 Report Page

🧠 Future Enhancements

🔮 Integrate voice-based AI career coaching

📈 Add deep learning model for skill clustering

🌍 Multi-language support (English + Indian languages)

🧩 Add real-time collaboration features for mentors

👨‍💻 Contributors
Role	Contributor
💡 Project Lead	Gowdru Nataraj
🤖 AI & Backend	ML + FastAPI Agent
🎨 Frontend & Animation	React + GSAP + Lottie Agent
🧠 LLM Reasoning	AI Career Coach Agent
🐳 DevOps & Deployment	Docker Agent
🪄 License

This project is licensed under the MIT License — feel free to use, modify, and share it with proper credit.

🌟 Star the Repo!

If you like this project, please ⭐ star it on GitHub to support future updates!

“Your career journey deserves AI magic. ✨ Let LifePathAI guide the way.”
