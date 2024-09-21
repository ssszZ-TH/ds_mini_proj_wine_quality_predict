<pre>
<span style="color: #FF6347;">      _</span>
<span style="color: #FF4500;">     | |</span>
<span style="color: #FFD700;">     | |===( )   ///////</span>
<span style="color: #ADFF2F;">     |_|   |||  | o o o|</span>
<span style="color: #7FFF00;">            |||  | o o o|</span>
<span style="color: #32CD32;">            |||  | o o o|</span>
<span style="color: #00FA9A;">            |||  '~~~~~~'</span>
<span style="color: #00CED1;">            |||</span>
<span style="color: #1E90FF;">            |||</span>
<span style="color: #4169E1;">            |||</span>
<span style="color: #6A5ACD;">            |||</span>
<span style="color: #8A2BE2;">            |||</span>
<span style="color: #9400D3;">  |\________///|</span>
<span style="color: #8B008B;">  |___________|</span>
</pre>

# <span style="color: red;">S</span><span style="color: green;">P</span><span style="color: blue;">A</span>


# เอกสารการใช้งานโปรเจกต์ Wine Quality Prediction

## คำอธิบายโปรเจกต์
โปรเจกต์นี้เป็นการพัฒนาแอปพลิเคชันสำหรับพยากรณ์คุณภาพของไวน์โดยใช้ข้อมูลทางเคมีของไวน์ เช่น ความเป็นกรด, กำมะถัน, และปริมาณแอลกอฮอล์ เป็นต้น แอปพลิเคชันนี้ถูกพัฒนาด้วย React สำหรับส่วนหน้าบ้าน และมีการใช้ Python และ Jupyter Notebook สำหรับการวิเคราะห์ข้อมูล

## โครงสร้างโปรเจกต์
- **backend**: โฟลเดอร์นี้ประกอบด้วยโค้ดสำหรับเซิร์ฟเวอร์ที่พัฒนาด้วย Python
- **frontend**: โฟลเดอร์นี้ประกอบด้วยโค้ดสำหรับส่วนหน้าบ้านที่พัฒนาด้วย React และ TypeScript
- **docker-compose.yml**: ไฟล์สำหรับตั้งค่า Docker Compose เพื่อรันโปรเจกต์

## การติดตั้งและการใช้งาน

### ข้อกำหนดเบื้องต้น
- ติดตั้ง [Docker](https://www.docker.com/) และ [Docker Compose](https://docs.docker.com/compose/)
- ติดตั้ง [Node.js](https://nodejs.org/) และ [npm](https://www.npmjs.com/)

### ขั้นตอนการติดตั้ง
1. **Clone โปรเจกต์จาก GitHub**
   ```bash
   git clone https://github.com/ssszZ-TH/ds_mini_proj_wine_quality_predict.git
   cd ds_mini_proj_wine_quality_predict
   ```

2. **ตั้งค่าและรัน Docker Compose**
   - รันคำสั่งต่อไปนี้เพื่อเริ่มต้นการทำงานของโปรเจกต์ด้วย Docker
   ```bash
   docker-compose up --build
   ```

3. **การเข้าถึงแอปพลิเคชัน**
   - เมื่อ Docker Compose รันเสร็จสิ้น คุณสามารถเข้าถึงแอปพลิเคชันได้ผ่านทางเว็บเบราว์เซอร์ที่ `http://localhost:3000`

## การใช้งาน
- เปิดแอปพลิเคชันในเว็บเบราว์เซอร์
- กรอกข้อมูลทางเคมีของไวน์ในฟอร์มที่ให้มา
- กดปุ่ม "Predict" เพื่อดูผลลัพธ์การพยากรณ์คุณภาพของไวน์

## หมายเหตุ
- โปรเจกต์นี้ยังไม่มีการเผยแพร่ release หรือ package ใด ๆ
- หากพบปัญหาหรือมีข้อสงสัยเพิ่มเติม สามารถติดต่อผ่าน GitHub Issues ได้

โปรดปรับแต่งเอกสารนี้เพิ่มเติมตามความต้องการเฉพาะของโปรเจกต์ของคุณ หากมีการเปลี่ยนแปลงหรือเพิ่มเติมฟีเจอร์ใหม่ ๆ ในอนาคต