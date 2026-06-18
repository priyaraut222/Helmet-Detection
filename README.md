# 🪖 Smart Helmet Detection System

An AI-powered Helmet Detection System built using *YOLOv8* and *Streamlit* to identify riders wearing helmets and riders without helmets from uploaded images.

The system performs object detection on uploaded images and highlights safety violations by classifying riders into:

* 🟢 With Helmet
* 🔴 Without Helmet

This project demonstrates the application of *Computer Vision, **Deep Learning, and **Model Deployment* for road safety monitoring.

---

# 🚀 Live Demo

*Try the Application Here:*

https://helmet-detection-76zflnymdv3fjpjixpfrde.streamlit.app/

---

# 📌 How It Works

text
Input Image
     │
     ▼
Streamlit File Uploader
     │
     ▼
YOLOv8 Custom-Trained Model
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


---

# 📂 Project Structure

text
Helmet-Detection/
│
├── app.py                     # Streamlit application
├── pretrained_model/
│   └── best.pt                # Trained YOLO model
│
├── train.ipynb                # Model training notebook
├── test.ipynb                 # Model evaluation notebook
│
├── yolo26n.pt                 # Pretrained YOLOv8 weights
├── requirements.txt           # Project dependencies
├── README.md                  # Documentation
└── .gitignore


---

# 🧠 Model Pipeline

### Dataset Preparation

* Helmet and No-Helmet rider images
* YOLO-format annotations
* Two-class object detection dataset

### Training Workflow

text
Dataset
   │
   ▼
YOLOv8n Base Model
   │
   ▼
Transfer Learning
   │
   ▼
Custom Training
   │
   ▼
best.pt Generated


### Inference Workflow

1. Upload an image.
2. The trained YOLOv8 model processes the image.
3. Riders are detected.
4. Bounding boxes are drawn around detected riders.
5. Helmet status is classified.
6. Detection statistics are displayed.

---
