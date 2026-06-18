# 🪖 Smart Helmet Detection System

An AI-powered Helmet Detection System built using **YOLO26** and **Streamlit** to identify riders wearing helmets and riders without helmets from uploaded images.

The system performs object detection on uploaded images and highlights safety violations by classifying riders into:

* 🟢 **With Helmet**
* 🔴 **Without Helmet**

This project demonstrates the application of **Computer Vision**, **Deep Learning**, and **Model Deployment** for road safety monitoring.

---

## 🚀 Live Demo

**Try the Application Here:**

🔗 https://helmet-detection-76zflnymdv3fijpixpfrde.streamlit.app/

---

## 📌 How It Works

```text
Input Image
     │
     ▼
Streamlit File Uploader
     │
     ▼
YOLOv26 Custom-Trained Model
     │
     ▼
Object Detection
     │
     ▼
Helmet Classification
     │
     ▼
Bounding Boxes + Confidence Scores
     │
     ▼
Detection Summary
```

---

## 📂 Project Structure

```text
Helmet-Detection/
│
├── app.py                     # Streamlit application
├── pretrained_model/
│   └── best.pt                # Trained YOLO26 model
│
├── train.ipynb                # Model training notebook
├── test.ipynb                 # Model evaluation notebook
│
├── yolo26n.pt                 # Pretrained YOLO26 weights
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
└── .gitignore
```

---

## 🧠 Model Pipeline

### Dataset Preparation

* Helmet and No-Helmet rider images
* YOLO-format annotations
* Two-class object detection dataset

### Training Workflow

```text
Dataset
   │
   ▼
YOLOv26n Base Model
   │
   ▼
Transfer Learning
   │
   ▼
Custom Training
   │
   ▼
best.pt Generated
```

### Inference Workflow

1. Upload an image.
2. The trained YOLO26 model processes the image.
3. Riders are detected and classified.
4. Bounding boxes are drawn around detected riders.
5. Helmet status is identified.
6. Detection statistics are displayed.

---

## ✨ Features

* Real-time Helmet Detection using YOLO26
* Upload and analyze custom images
* Bounding box visualization
* Confidence score display
* Rider count summary
* Safety alerts for riders without helmets
* Interactive Streamlit interface
* Cloud deployment using Streamlit Community Cloud
* GitHub version control integration

---

## 🛠️ Tech Stack

| Layer               | Technology  |
| ------------------- | ----------- |
| Frontend            | Streamlit   |
| Deep Learning       | YOLO26     |
| Computer Vision     | OpenCV      |
| Image Processing    | Pillow      |
| Numerical Computing | NumPy       |
| Model Framework     | Ultralytics |
| Language            | Python      |

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/priyaraut222/Helmet-Detection.git
cd Helmet-Detection
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux/macOS

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📊 Output

The application provides:

* Annotated image with detections
* Helmet / No Helmet classification
* Detection confidence scores
* Rider count summary
* Safety alerts for safety violations

---

## 🎯 Applications

* Traffic Surveillance
* Smart City Monitoring
* Road Safety Enforcement
* Automated Violation Detection
* Transportation Safety Analytics

---

## 🔮 Future Scope

* Video Detection Support
* Real-Time CCTV Integration
* Number Plate Recognition (ANPR)
* Automated Fine Generation
* Dashboard Analytics
* Cloud-Based Monitoring System
* Mobile Application Integration

---

## ⭐ Project Highlights

* Custom-Trained YOLOv26 Model
* End-to-End Machine Learning Deployment
* Computer Vision-Based Safety Monitoring
* Interactive Web Application
* Streamlit Cloud Deployment
* GitHub Hosted Project
* Real-Time Helmet Compliance Detection

---

## 📜 License

This project is intended for educational and research purposes.
