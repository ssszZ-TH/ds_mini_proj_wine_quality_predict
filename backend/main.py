from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import List, Annotated
from joblib import load
from fastapi.middleware.cors import CORSMiddleware

# กำหนดชนิดของข้อมูล input
class WineQuality(BaseModel):
    data: Annotated[List[List[float]], Field(min_length=1)]

    class Config:
        json_schema_extra = {
            "example": {
                "data": [[7.4, 0.7, 0.0, 1.9, 0.076, 11.0, 34.0, 0.9978, 3.51, 0.56, 9.4]]
            }
        }

# สร้าง instance ของแอป
app = FastAPI(title="Wine Quality ML API", description="API for wine-qualities ml model", version="1.0")

# เพิ่ม CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # อนุญาตทุก origins
    allow_credentials=True,
    allow_methods=["*"],  # อนุญาตทุก HTTP methods
    allow_headers=["*"],  # อนุญาตทุก headers
)

# โหลดโมเดลในช่วงเริ่มต้นของแอป
@app.on_event("startup")
async def load_model():
    app.model = load('./models/random_forest_super_reduced_model.pkl')  # โหลดโมเดลและเก็บไว้ใน app.model

# ฟังก์ชันสำหรับการพยากรณ์
@app.post("/predict")
async def predict(user_input: WineQuality):
    data = user_input.data
    result = app.model.predict(data)
    return {"prediction": result.tolist()}  # ส่งกลับเป็น dict เพื่อให้ API response ดียิ่งขึ้น

# รันเซิร์ฟเวอร์ด้วยคำสั่ง
# uvicorn main:app --reload
