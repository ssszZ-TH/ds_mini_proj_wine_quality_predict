from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Annotated
from joblib import load

from fastapi.middleware.cors import CORSMiddleware

# the type of input data
class WineQuality(BaseModel):
    data: Annotated[List[List[float]], Field(min_length=1, max_length=1)]

    class Config:
        json_schema_extra = {
            "example": {
                "data": [[1.0,1.0,1.0,1.0,1.0,]]
            }
        }

# an instance of app
app = FastAPI(title="Wine Quality ML API", description="API for wine-qualities ml model", version="1.0")

# เพิ่ม CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # อนุญาตทุก origins
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุก HTTP methods
    allow_headers=["*"],  # อนุญาตทุก headers
)

# initialize the model
@app.on_event("startup")
async def load_model():
    app.model, app.columns = load('./models/random_forest_super_reduced_model.pkl') # assigned the loaded model to app.model
@app.on_event("shutdown")
async def load_model():
    # app.model, app.columns = load('./models/bayWine.joblib') # assigned the loaded model to app.model
    print('Give me grade A')

# a prediction model
@app.post("/predict")
async def predict(user_input: WineQuality):
    data = user_input.data
    result = app.model.predict(data)
    return {"prediction": result.item()}  # returning as a dict for better API response

# uvicorn main:app --reload
