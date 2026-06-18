import streamlit as st
from ultralytics import YOLO
from PIL import Image
import tempfile
import os
import cv2
import numpy as np

# ==========================================
# PAGE CONFIG
# ==========================================
st.set_page_config(
    page_title="Smart Helmet Detection System",
    page_icon="🪖",
    layout="wide"
)

# ==========================================
# LOAD MODEL
# ==========================================
model = YOLO("runs/detect/train-3/weights/best.pt")

# ==========================================
# LIVE DETECTION FUNCTION
# ==========================================
def run_live_detection():

    cap = cv2.VideoCapture(0)

    while True:

        success, frame = cap.read()

        if not success:
            break

        results = model.predict(
            frame,
            conf=0.3,
            verbose=False
        )

        result = results[0]

        for box in result.boxes:

            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            class_name = result.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            if class_name == "With Helmet":
                color = (0, 255, 0)      # Green
            else:
                color = (0, 0, 255)      # Red

            cv2.rectangle(
                frame,
                (x1, y1),
                (x2, y2),
                color,
                3
            )

            cv2.putText(
                frame,
                f"{class_name} {conf:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

        cv2.imshow(
            "Live Helmet Detection (Press Q to Exit)",
            frame
        )

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

# ==========================================
# HEADER
# ==========================================
st.title("🪖 Smart Helmet Detection System")

st.markdown("""
### AI-based Detection of Riders Wearing Helmets and Riders Without Helmets
""")

st.markdown("---")

# ==========================================
# TABS
# ==========================================
tab1, tab2 = st.tabs(
    ["📷 Image Detection", "🎥 Live Camera Detection"]
)

# ==========================================
# IMAGE DETECTION
# ==========================================
with tab1:

    uploaded_file = st.file_uploader(
        "Upload an Image",
        type=["jpg", "jpeg", "png"]
    )

    if uploaded_file is not None:

        image = Image.open(
            uploaded_file
        ).convert("RGB")

        st.subheader("Original Image")

        st.image(
            image,
            use_container_width=True
        )

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".jpg"
        ) as tmp:

            image.save(tmp.name)
            temp_path = tmp.name

        results = model.predict(
            source=temp_path,
            conf=0.3,
            iou=0.5
        )

        result = results[0]

        annotated = np.array(image).copy()

        with_helmet = 0
        without_helmet = 0

        for box in result.boxes:

            cls_id = int(box.cls[0])
            confidence = float(box.conf[0])

            class_name = result.names[cls_id]

            x1, y1, x2, y2 = map(
                int,
                box.xyxy[0]
            )

            if class_name == "With Helmet":

                with_helmet += 1

                color = (0, 255, 0)

            else:

                without_helmet += 1

                color = (255, 0, 0)

            cv2.rectangle(
                annotated,
                (x1, y1),
                (x2, y2),
                color,
                3
            )

            cv2.putText(
                annotated,
                f"{class_name} {confidence:.2f}",
                (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2
            )

        st.subheader("Detection Result")

        st.markdown("""
🟢 **With Helmet**

🔴 **Without Helmet**
""")

        st.image(
            annotated,
            use_container_width=True
        )

        col1, col2 = st.columns(2)

        with col1:
            st.success(
                f"🟢 With Helmet: {with_helmet}"
            )

        with col2:
            st.error(
                f"🔴 Without Helmet: {without_helmet}"
            )

        st.markdown("---")

        if without_helmet > 0:

            st.error(
                f"🚨 ALERT: {without_helmet} Rider(s) Without Helmet Detected!"
            )

        elif with_helmet > 0:

            st.success(
                f"✅ {with_helmet} Rider(s) Wearing Helmet"
            )

        else:

            st.warning(
                "⚠️ No Riders Detected"
            )

        st.subheader("Detection Details")

        if len(result.boxes) == 0:

            st.write(
                "No detections found."
            )

        else:

            for i, box in enumerate(
                result.boxes,
                start=1
            ):

                cls_id = int(box.cls[0])

                confidence = float(
                    box.conf[0]
                )

                class_name = result.names[
                    cls_id
                ]

                st.write(
                    f"Detection {i} | "
                    f"{class_name} | "
                    f"Confidence: {confidence:.2f}"
                )

        os.remove(temp_path)

# ==========================================
# LIVE CAMERA DETECTION
# ==========================================
with tab2:

    st.subheader(
        "🎥 Live Helmet Detection"
    )

    st.info(
        "Press START to open webcam. Press Q to stop."
    )

    if st.button(
        "▶ Start Live Detection"
    ):

        run_live_detection()

st.markdown("---")

st.caption(
    "YOLOv8 Based Helmet Detection System"
)