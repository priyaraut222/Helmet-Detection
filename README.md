# 🪖 Smart Helmet Detection System

## 📌 Overview

The Smart Helmet Detection System is a computer vision application developed using YOLO (You Only Look Once) object detection technology to identify riders wearing helmets and riders without helmets in real-time.

The system enhances road safety monitoring by automatically detecting helmet compliance from images and live webcam feeds. It provides visual alerts for riders not wearing helmets and can be used as a foundation for intelligent traffic surveillance systems.

---

## 🚀 Features

* 🪖 Detects riders wearing helmets
* ⚠️ Detects riders without helmets
* 📷 Image-based detection
* 🎥 Live webcam detection using OpenCV
* 📊 Real-time helmet count
* 🚨 Safety alerts for riders without helmets
* 🎯 Confidence score display
* 🌐 Interactive Streamlit web application
* 🔴 Red bounding boxes for "Without Helmet"
* 🟢 Green bounding boxes for "With Helmet"

---

## 🛠️ Technologies Used

* Python
* YOLO Object Detection
* OpenCV
* Streamlit
* NumPy
* MLflow

---

## 📂 Dataset

The model was trained on a custom annotated dataset containing two classes:

| Class ID | Class Name     |
| -------- | -------------- |
| 0        | With Helmet    |
| 1        | Without Helmet |

The dataset consists of labeled rider images with corresponding bounding box annotations in YOLO format.

---

## 🧠 Model Training

The model was trained using the YOLO framework with custom helmet detection data.

### Training Configuration

* Image Size: 640 × 640
* Classes: 2
* Framework: YOLO
* Detection Type: Object Detection

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/helmet-detection.git
cd helmet-detection
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

---

## 📷 Image Detection

1. Upload an image.
2. The model detects riders with and without helmets.
3. Detection results are displayed with bounding boxes.
4. Helmet statistics and alerts are generated automatically.

---

## 🎥 Live Camera Detection

1. Open the Live Camera Detection tab.
2. Click **Start Live Detection**.
3. The webcam feed opens using OpenCV.
4. Real-time detections are displayed.
5. Press **Q** to exit the webcam window.

---

## 📊 Output

The application provides:

* Total riders wearing helmets
* Total riders without helmets
* Detection confidence scores
* Real-time safety alerts
* Visual detection results

---

## 🚨 Safety Alert System

The system automatically generates alerts whenever riders without helmets are detected.

Example:

```text
ALERT: 2 Riders Without Helmet Detected
```

---

## 🔮 Future Enhancements

* Vehicle detection integration
* Number plate recognition
* Traffic analytics dashboard
* Cloud deployment
* Mobile application support
* Automated violation reporting

---

## 🎯 Applications

* Smart Traffic Monitoring
* Road Safety Enforcement
* Intelligent Transportation Systems
* Traffic Surveillance
* Helmet Compliance Monitoring

---

