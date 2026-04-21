# 🚦 Traffic Violation Detection System (ML + Computer Vision)

An end-to-end computer vision system to automatically detect traffic violations such as **no helmet** and **triple riding** from video feeds using deep learning and tracking techniques.

---

## 🔍 Overview

This project simulates a smart city traffic monitoring system by processing video streams to:

- Detect vehicles and riders
- Track objects across frames
- Identify traffic violations
- Extract license plate numbers (OCR)
- Log violations in a structured format

---

## 🧠 System Pipeline


Video Input
↓
Object Detection (YOLOv8)
↓
Multi-Object Tracking (DeepSORT)
↓
Violation Detection Engine
↓
License Plate Recognition (OCR)
↓
Dashboard + Logs


---

## 🚨 Features

- 🚗 Vehicle Detection (cars, bikes, buses)
- 🪖 Helmet Detection (rule-based logic)
- 👥 Triple Riding Detection
- 🔢 License Plate Recognition (EasyOCR)
- 📊 Flask Dashboard for monitoring
- 📁 Automatic violation evidence storage

---

## 🛠️ Tech Stack

- Python
- YOLOv8 (Ultralytics)
- OpenCV
- DeepSORT
- EasyOCR
- Flask
- Pandas, NumPy

---

## 📂 Project Structure


traffic-violation-ai/
│
├── detection/ # YOLO detection
├── tracking/ # DeepSORT tracking
├── violations/ # Rule-based logic
├── ocr/ # License plate recognition
├── dashboard/ # Flask app
├── videos/ # Input videos
├── output/ # Saved violations
├── requirements.txt
└── README.md


---

## ▶️ Getting Started

### 1. Clone Repository

```bash
git clone https://github.com/your-username/traffic-violation-ai.git
cd traffic-violation-ai
2. Create Virtual Environment
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows
3. Install Dependencies
pip install -r requirements.txt
4. Run Detection
python detection/detect.py
📸 Sample Output
Detected vehicles with bounding boxes
Saved violation images in /output
Logs generated with timestamp and violation type
📊 Results
Achieved ~3–5 FPS on CPU-based system
Successfully detected:
No helmet violations
Triple riding cases
Demonstrated scalable pipeline for smart traffic systems
🚀 Future Improvements
Red light violation detection
Speed estimation
Real-time CCTV integration (RTSP)
Cloud deployment (AWS/GCP)
CI/CD pipeline integration
📌 Use Cases
Smart city traffic monitoring
Automated challan generation
Traffic analytics & reporting
Law enforcement assistance
🤝 Contributing

Contributions are welcome! Feel free to open issues or submit PRs.
