from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import mlflow.sklearn
import mlflow

mlflow.set_tracking_uri("http://localhost:5000")
app = FastAPI()

model_name = 'spotify_prediction_testing'
model_version = '2'
# model = mlflow.xgboost.load_model(f"models:/{model_name}/{model_version}")
model = mlflow.sklearn.load_model(f"models:/{model_name}/{model_version}")

class InputData(BaseModel):
    danceability: float
    energy: float
    loudness: float
    speechiness: float
    acousticness: float
    instrumentalness: float
    liveness: float
    valence: float
    tempo: float
    duration_ms: int
    year: int
    genre: str
    key: int
    mode: int
    time_signature: int

@app.post('/predict')
async def predict(data: InputData):
    input_df = pd.DataFrame([data.model_dump()])

    prediction = model.predict(input_df).tolist()
    return {'prediction': prediction}