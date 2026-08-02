import joblib 

from fastapi import FastAPI
from pydantic import BaseModel,Field
import pandas as pd
from typing import Literal
from fastapi.middleware.cors import CORSMiddleware

model = joblib.load("Mental_Heath_Model.pkl")
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

#A.Pydantic model - so pydantic is simple the midway which has a json file fo valide inputs like it age someone eneter string it will not accept so we declare age:int ...so pydantic is useful for it ..pydantic acts as security input for API's

top_countries = ['Other','India','USA','Canada','Australia','UK','Germany','Mexico','Turkey','France']


class StudentData(BaseModel):
    
    age: int = Field(...,ge = 10,le = 100) #(...) -> means mandatory
    gender: Literal['Male','Female'] 
    country: str
    academic_level: Literal['Undergraduate', 'Graduate', 'High School']
    most_used_platform: Literal['Facebook', 'LinkedIn', 'Instagram', 'Snapchat', 'Twitter',
       'YouTube', 'TikTok', 'LINE', 'KakaoTalk', 'VKontakte', 'WhatsApp',
       'WeChat']
    purpose_of_use: Literal['Networking', 'Education', 'Entertainment', 'News']
    avg_daily_usage_hours: float = Field(...,ge=0,le=24)
    daily_unlocks: int = Field(...,ge=0)
    study_hours: float = Field(...,ge=0,le=24)
    physical_activity_hours:float = Field(...,ge=0,le=2)
    sleep_hours_per_night: float = Field(...,ge=0,le=24)
    stress_level: Literal['Medium', 'Low', 'Very High', 'High']
    
    
#describe what we send back i. response body

class PredictionResponse(BaseModel):
    predicted_mental_health_score : float
    
    


@app.get('/')
def greet():
    return {'Welcome to Sarthak Life'}


@app.post('/predict',response_model = PredictionResponse)
def predict(data:StudentData):
    
    country_group = data.country if data.country in top_countries else "Other"
    
    input_row=pd.DataFrame([{
        
        'Age' : data.age,
        'Gender' : data.gender,
        'Country' : data.country,
        'Academic_Level' : data.academic_level,
        'Most_Used_Platform' :data.most_used_platform,
        'Purpose_Of_Use' : data.purpose_of_use,
        'Avg_Daily_Usage_Hours' : data.avg_daily_usage_hours,
        'Daily_Unlocks' : data.daily_unlocks,
        'Study_Hours' : data.study_hours,
        'Physical_Activity_Hours' : data.physical_activity_hours,
        'Sleep_Hours_Per_Night':data.sleep_hours_per_night,
        'Stress_Level':data.stress_level,
        
        'Grouped_Country': country_group
        
    }])
    
    
    prediction = model.predict(input_row)[0]
    
    
    return PredictionResponse(predicted_mental_health_score=round(float(prediction),2))
    
