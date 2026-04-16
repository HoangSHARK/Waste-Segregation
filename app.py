import streamlit as st
import os
import tensorflow as tf
import numpy as np
from PIL import Image

st.markdown("""
<style>
    .main {
        background-color: #f4f6fa;
    }
    .title {
        font-size: 32px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        margin-bottom: 10px;
    }
    .subtitle {
        text-align: center;
        color: #7f8c8d;
        margin-bottom: 25px;
        font-size: 16px;
    }
    .result-box {
        padding: 18px;
        border-radius: 12px;
        background-color: white;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        margin-top: 20px;
    }
    .good { color: #27ae60; }
    .bad { color: #c0392b; }
</style>
""", unsafe_allow_html=True)


model = tf.keras.models.load_model(r"D:\Do_an_2\Tuần 6\mobilenet_model.h5")

def preprocess_image(img):
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    return img


st.markdown('<div class="title">Phân Loại Rác Thải MobileNetV2</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Tải ảnh lên và hệ thống sẽ tự động phân loại</div>', unsafe_allow_html=True)


uploaded_file = st.file_uploader("📤 Chọn ảnh", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:

    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="📸 Ảnh bạn đã tải", use_container_width=True)

    img = preprocess_image(image)
    pred = model.predict(img)[0][0]


    nonbio_folder = "D:/Do_an_2/Tuần 6/Non_biodegradable"
    bio_folder = "D:/Do_an_2/Tuần 6/Biodegradable"

    os.makedirs(nonbio_folder, exist_ok=True)
    os.makedirs(bio_folder, exist_ok=True)

    if pred > 0.5:
        result_text = "Rác thải không phân hủy được"
        result_class = "bad"
        save_path = os.path.join(nonbio_folder, uploaded_file.name)
        image.save(save_path)
        moved_text = "Đã chuyển ảnh vào thư mục non_biodegradable"
    else:
        result_text = "Rác thải phân hủy được"
        result_class = "good"
        save_path = os.path.join(bio_folder, uploaded_file.name)
        image.save(save_path)
        moved_text = "Đã chuyển ảnh vào thư mục biodegradable"


    st.markdown(
        f'<div class="result-box {result_class}">{result_text}</div>',
        unsafe_allow_html=True
    )

    st.info(f"📁 {moved_text}")
    st.success(f"📌 Ảnh đã lưu tại:\n{save_path}")
