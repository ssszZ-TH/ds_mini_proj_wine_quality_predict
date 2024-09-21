import React, { useEffect, useState } from 'react';
// นำเข้า component และ hooks จาก React และ Material-UI

import { 
  TextField, 
  Button, 
  Card, 
  CardContent, 
  CardActions, 
  Typography, 
  Grid 
} from '@mui/material';
// นำเข้า component ที่จำเป็นจาก Material-UI สำหรับการสร้าง UI

// กำหนด interface สำหรับข้อมูลฟอร์ม
interface FormData {
  fixedAcidity: string;
  volatileAcidity: string;
  totalSulfurDioxide: string;
  sulphates: string;
  alcohol: string;
}

// กำหนดค่าเริ่มต้นสำหรับข้อมูลฟอร์ม
const initialFormData: FormData = {

  fixedAcidity: '',
  volatileAcidity: '',
  totalSulfurDioxide: '',
  sulphates: '',
  alcohol: '',
};

// สร้าง component หลักของฟอร์ม
const WineQualityForm: React.FC = () => {
  // ใช้ useState เพื่อจัดการสถานะของข้อมูลฟอร์มและผลลัพธ์การพยากรณ์
  const [formData, setFormData] = useState<FormData>(initialFormData);
  const [prediction, setPrediction] = useState<string | null>(null);

  // ใช้ useEffect เพื่อ debug ดูข้อมูลฟอร์มทุกครั้งที่มีการเปลี่ยนแปลง
  useEffect(() => {
    console.log(formData);
  }, [formData]);

  // ฟังก์ชันสำหรับจัดการการเปลี่ยนแปลงในช่อง input
  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value // อัปเดตค่าของฟิลด์ที่เปลี่ยน
    }));
  };

  // ฟังก์ชันสำหรับจัดการเมื่อฟอร์มถูกส่ง
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault(); // ป้องกันการ reload หน้าเว็บ

    // เตรียม payload ที่จะส่งไปยังเซิร์ฟเวอร์
    const payload = {
      data: [Object.values(formData).map(Number)] // แปลงค่าจาก string เป็น number
    };
    console.log('shoot service payload =', payload);
    
    try {
      // ส่งคำร้องขอไปยังเซิร์ฟเวอร์เพื่อพยากรณ์
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(payload),
      });

      if (response.ok) {
        // ถ้าการร้องขอสำเร็จ ให้แสดงผลลัพธ์การพยากรณ์
        const result = await response.json();
        console.log('Result:', result);
        setPrediction(result.prediction[0] === 1 ? 'Good Quality' : 'Poor Quality');
      } else {
        setPrediction('Error occurred'); // กรณีเกิดข้อผิดพลาด
      }
    } catch (error) {
      console.error('Error:', error);
      setPrediction('Error occurred'); // กรณีเกิดข้อผิดพลาดในการเชื่อมต่อ
    }
  };

  return (
    <Card sx={{ maxWidth: 600, margin: 'auto', mt: 5 }}>
      <CardContent>
        <Typography variant="h5" component="div" gutterBottom>
          Wine Quality Prediction
        </Typography>
        <form onSubmit={handleSubmit}>
          <Grid container spacing={2}>
            {Object.entries(formData).map(([key, value]) => (
              <Grid item xs={12} sm={6} key={key}>
                <TextField
                  fullWidth
                  label={key.replace(/([A-Z])/g, ' $1').trim()} // เปลี่ยนชื่อฟิลด์ให้มีช่องว่างระหว่างคำ ถ้าเจอตัวอักษรตัวใหญ่ ให้เติม space ด้านหน้า
                  type="number"
                  // step="0.01"
                  name={key}
                  value={value}
                  onChange={handleInputChange}
                  required
                  variant="outlined"
                />
              </Grid>
            ))}
          </Grid>
          <CardActions sx={{ justifyContent: 'center', mt: 2 }}>
            <Button type="submit" variant="contained" color="primary">
              Predict
            </Button>
          </CardActions>
        </form>
      </CardContent>
      {prediction && (
        <CardContent>
          <Typography variant="h6" align="center">
            Prediction: {prediction}
          </Typography>
        </CardContent>
      )}
    </Card>
  );
};

export default WineQualityForm;
