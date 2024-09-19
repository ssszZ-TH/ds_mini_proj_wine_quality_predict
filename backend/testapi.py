import aiohttp
import asyncio
import json
import random

# URL ของ API
url = 'http://127.0.0.1:5000/predict'


    
# ฟังก์ชันสร้าง payload แบบสุ่มที่มีโอกาสได้ prediction เป็น 1 สูง
def generate_likely_good_wine():
    return [
        round(random.uniform(0, 100), 2),    # alcohol
        round(random.uniform(0, 100), 2),      # volatile acidity
        round(random.uniform(0, 100), 2),      # citric acid
        round(random.uniform(0, 100), 2),      # residual sugar
        round(random.uniform(0, 100), 2),    # chlorides
        round(random.uniform(0, 100), 2),    # free sulfur dioxide
        round(random.uniform(0, 100), 2),    # total sulfur dioxide
        round(random.uniform(0, 100), 2),  # density
        round(random.uniform(0, 100), 2),      # pH
        round(random.uniform(0, 100), 2),      # sulphates
        round(random.uniform(0, 100), 2),    # alcohol (again, for variety)
    ]

# สร้าง payloads
payloads = []

# เพิ่ม payloads แบบสุ่มอีก 20 ชุด
for _ in range(100):
    payloads.append({"data": [generate_likely_good_wine()]})

print(f'payloads len = {len(payloads)}')
# ฟังก์ชันสำหรับทดสอบ API ด้วย payload แบบ async
async def test_api(session, payload):
    try:
        async with session.post(url, data=json.dumps(payload), headers={"Content-Type": "application/json"}) as response:
            if response.status == 200:
                result = await response.json()
                print(f"Payload: {payload} => Response: {result}")
            else:
                print(f"Payload: {payload} => Failed with status code: {response.status}")
    except Exception as e:
        print(f"Payload: {payload} => Exception: {str(e)}")

# ฟังก์ชันหลักสำหรับรันการทดสอบแบบ async
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [test_api(session, payload) for payload in payloads]
        await asyncio.gather(*tasks)

# รันโปรแกรม
if __name__ == '__main__':
    asyncio.run(main())
