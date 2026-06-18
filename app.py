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
model = YOLO("pretrained_model/best.pt")

# ==========================================
# HEADER
# ==========================================
st.title("🪖 Smart Helmet Detection System")

st.markdown("""
### AI-Based Detection of Riders Wearing Helmets and Riders Without Helmets
""")

st.markdown("---")

# ==========================================
# TABS
# ==========================================
tab1, tab2 = st.tabs(
    ["📷 Image Detection", "🎥 Video Detection"]
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

        os.remove(temp_path)

# ==========================================
# VIDEO DETECTION
# ==========================================
with tab2:

    st.subheader("🎥 Video Helmet Detection")

    uploaded_video = st.file_uploader(
        "Upload a Video",
        type=["mp4", "avi", "mov"],
        key="video"
    )

    if uploaded_video is not None:

        st.video(uploaded_video)

        if st.button("🚀 Process Video"):

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".mp4"
            ) as temp_video:

                temp_video.write(
                    uploaded_video.read()
                )

                video_path = temp_video.name

            cap = cv2.VideoCapture(video_path)

            width = int(
                cap.get(cv2.CAP_PROP_FRAME_WIDTH)
            )

            height = int(
                cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
            )

            fps = cap.get(
                cv2.CAP_PROP_FPS
            )

            output_path = "processed_video.mp4"

            fourcc = cv2.VideoWriter_fourcc(
                *'mp4v'
            )

            out = cv2.VideoWriter(
                output_path,
                fourcc,
                fps,
                (width, height)
            )

            total_frames = int(
                cap.get(
                    cv2.CAP_PROP_FRAME_COUNT
                )
            )

            progress_bar = st.progress(0)

            frame_count = 0

            while cap.isOpened():

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
                    confidence = float(box.conf[0])

                    class_name = result.names[
                        cls_id
                    ]

                    x1, y1, x2, y2 = map(
                        int,
                        box.xyxy[0]
                    )

                    if class_name == "With Helmet":
                        color = (0, 255, 0)
                    else:
                        color = (0, 0, 255)

                    cv2.rectangle(
                        frame,
                        (x1, y1),
                        (x2, y2),
                        color,
                        3
                    )

                    cv2.putText(
                        frame,
                        f"{class_name} {confidence:.2f}",
                        (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        color,
                        2
                    )

                out.write(frame)

                frame_count += 1

                progress_bar.progress(
                    min(
                        frame_count / total_frames,
                        1.0
                    )
                )

            cap.release()
            out.release()

            st.success(
                "✅ Video Processed Successfully!"
            )

            st.video(output_path)

            with open(
                output_path,
                "rb"
            ) as file:

                st.download_button(
                    label="📥 Download Processed Video",
                    data=file,
                    file_name="helmet_detection_output.mp4",
                    mime="video/mp4"
                )

st.markdown("---")

st.caption(
    "YOLOv8 Based Smart Helmet Detection System"
)