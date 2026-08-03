import joblib
import pandas as pd

from typing import Literal

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from pydantic import BaseModel, Field

# --------------------------------------------------
# Load Trained Model
# --------------------------------------------------

model = joblib.load("Mental_Heath_Model.pkl")

# --------------------------------------------------
# FastAPI App
# --------------------------------------------------

app = FastAPI(title="Mental Health Score Predictor API")

# --------------------------------------------------
# CORS
# --------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --------------------------------------------------
# Static Files & HTML Templates
# --------------------------------------------------

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

# --------------------------------------------------
# Countries
# --------------------------------------------------

top_countries = [
    "Other",
    "India",
    "USA",
    "Canada",
    "Australia",
    "UK",
    "Germany",
    "Mexico",
    "Turkey",
    "France",
]

# --------------------------------------------------
# Request Model
# --------------------------------------------------

class StudentData(BaseModel):

    age: int = Field(..., ge=10, le=100)

    gender: Literal["Male", "Female"]

    country: str

    academic_level: Literal[
        "Undergraduate",
        "Graduate",
        "High School",
    ]

    most_used_platform: Literal[
        "Facebook",
        "Instagram",
        "LinkedIn",
        "Snapchat",
        "TikTok",
        "Twitter",
        "WhatsApp",
        "WeChat",
        "YouTube",
        "LINE",
        "KakaoTalk",
        "VKontakte",
    ]

    purpose_of_use: Literal[
        "Education",
        "Entertainment",
        "Networking",
        "News",
    ]

    avg_daily_usage_hours: float = Field(..., ge=0, le=24)

    daily_unlocks: int = Field(..., ge=0)

    study_hours: float = Field(..., ge=0, le=24)

    physical_activity_hours: float = Field(..., ge=0, le=24)

    sleep_hours_per_night: float = Field(..., ge=0, le=24)

    stress_level: Literal[
        "Low",
        "Medium",
        "High",
        "Very High",
    ]


# --------------------------------------------------
# Response Model
# --------------------------------------------------

class PredictionResponse(BaseModel):
    predicted_mental_health_score: float


# --------------------------------------------------
# Home Page
# --------------------------------------------------

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request},
    )


# --------------------------------------------------
# Prediction API
# --------------------------------------------------

@app.post(
    "/predict",
    response_model=PredictionResponse,
)
def predict(data: StudentData):

    country_group = (
        data.country
        if data.country in top_countries
        else "Other"
    )

    input_row = pd.DataFrame(
        [
            {
                "Age": data.age,
                "Gender": data.gender,
                "Country": data.country,
                "Academic_Level": data.academic_level,
                "Most_Used_Platform": data.most_used_platform,
                "Purpose_Of_Use": data.purpose_of_use,
                "Avg_Daily_Usage_Hours": data.avg_daily_usage_hours,
                "Daily_Unlocks": data.daily_unlocks,
                "Study_Hours": data.study_hours,
                "Physical_Activity_Hours": data.physical_activity_hours,
                "Sleep_Hours_Per_Night": data.sleep_hours_per_night,
                "Stress_Level": data.stress_level,
                "Grouped_Country": country_group,
            }
        ]
    )

    prediction = model.predict(input_row)[0]

    return PredictionResponse(
        predicted_mental_health_score=round(float(prediction), 2)
    )