from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import time

app = FastAPI()

# --- CORS Setup ---
origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Models ---
class UserInput(BaseModel):
    gpa: float
    skills: list[str]
    interests: list[str]

class Feedback(BaseModel):
    feedback_text: str

# --- Rule-Based Roadmap System ---
def get_career_roadmap(career: str):
    roadmaps = {
        "AI Engineer": {
            "title": "Your Rule-Based Career Roadmap: AI Engineer",
            "summary": "The path to becoming an AI Engineer is challenging but rewarding. Based on our rules, your profile is a strong match. This path focuses on building a strong foundation in computer science and mathematics.",
            "roadmap": [
                {"milestone": "Year 1: Core Programming", "description": "Master Python and key libraries like NumPy and Pandas. Solidify your understanding of data structures and algorithms."},
                {"milestone": "Year 2: Machine Learning Fundamentals", "description": "Study core ML concepts (e.g., regression, classification). Complete Andrew Ng's Machine Learning course."},
                {"milestone": "Year 3: Deep Learning Specialization", "description": "Focus on neural networks, TensorFlow/PyTorch. Build a project, like an image classifier."},
                {"milestone": "Year 4: Portfolio and Interviews", "description": "Create a portfolio of 3-5 diverse AI projects. Practice coding challenges and system design questions."}
            ]
        },
        "Data Analyst": {
            "title": "Your Rule-Based Career Roadmap: Data Analyst",
            "summary": "As a Data Analyst, you will turn data into actionable insights. This path emphasizes statistical knowledge and data visualization skills.",
            "roadmap": [
                {"milestone": "Year 1: Excel & SQL Mastery", "description": "Become proficient in advanced Excel functions and master SQL for data querying and manipulation."},
                {"milestone": "Year 2: Statistics & Python", "description": "Learn statistical analysis and hypothesis testing. Use Python's Pandas library for data analysis."},
                {"milestone": "Year 3: Visualization Tools", "description": "Master a BI tool like Tableau or Power BI. Create a dashboard for a public dataset."},
                {"milestone": "Year 4: Business Acumen", "description": "Develop an understanding of business operations. Focus on internships and projects with clear business impact."}
            ]
        },
        "Software Engineer": {
            "title": "Your Rule-Based Career Roadmap: Software Engineer",
            "summary": "The Software Engineer path is about building robust and scalable applications. This roadmap focuses on software development principles.",
            "roadmap": [
                {"milestone": "Year 1: CS Fundamentals", "description": "Learn a versatile language like Java or JavaScript. Understand object-oriented programming and web fundamentals (HTML/CSS)."},
                {"milestone": "Year 2: Frameworks & Databases", "description": "Learn a backend framework (e.g., Spring, Node.js) and a frontend framework (e.g., React). Understand how to work with databases."},
                {"milestone": "Year 3: System Design & DevOps", "description": "Study system design principles for scalable applications. Learn about CI/CD, Docker, and cloud platforms like AWS."},
                {"milestone": "Year 4: Open Source & Specialization", "description": "Contribute to an open-source project. Consider specializing in an area like mobile development, cybersecurity, or backend systems."}
            ]
        }
    }
    # Return the specific roadmap, or a default if not found
    return roadmaps.get(career, roadmaps["Software Engineer"]) # Default to Software Engineer

# --- API Endpoints ---
@app.get("/health")
def read_root():
    return {"status": "healthy"}

@app.post("/predict")
def predict_career(user_input: UserInput):
    """
    Mock endpoint to predict career paths.
    Uses a rule-based system for the roadmap.
    """
    time.sleep(1)  # Simulate processing time
    
    # Mock prediction - in a real app, this comes from the ML model
    top_careers_data = [
        {"career": "AI Engineer", "prob": 0.82},
        {"career": "Data Analyst", "prob": 0.11},
        {"career": "Software Engineer", "prob": 0.07}
    ]
    
    top_career = top_careers_data[0]
    top_career_name = top_career["career"]
    top_career_prob = top_career["prob"]

    # Rule-based animation mood
    animation_mood = "contemplative_start"
    if top_career_prob > 0.8:
        animation_mood = "optimistic_rise"
    elif top_career_prob > 0.5:
        animation_mood = "steady_growth"

    return {
        "top_careers": top_careers_data,
        "shap_summary": [
            {"feature": "analytical_index", "contribution": 0.21},
            {"feature": "python_skill", "contribution": 0.18},
            {"feature": "gpa", "contribution": 0.15},
            {"feature": "interest_in_ai", "contribution": 0.12},
        ],
        "roadmap_details": get_career_roadmap(top_career_name),
        "animation_theme": "growth_curve",
        "animation_mood": animation_mood
    }

@app.post("/report")
def generate_report(user_input: UserInput):
    """
    Mock endpoint for generating a PDF report.
    """
    time.sleep(2)  # Simulate report generation
    return {"report_url": "http://example.com/mock_report.pdf"}

@app.post("/feedback")
def receive_feedback(feedback: Feedback):
    """
    Mock endpoint to receive user feedback.
    """
    print(f"Received feedback: {feedback.feedback_text}")
    return {"message": "Thank you for your feedback!"}
