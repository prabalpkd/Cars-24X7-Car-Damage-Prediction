import streamlit as st
from model_helper import predict


# Center aligned Title
st.markdown("<h1 style='text-align: center;'>🚗Cars 24x7🚗</h1>", unsafe_allow_html=True)
# Center aligned Header
st.markdown("<h2 style='text-align: center;'>Car Damage Detection</h2>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload a file", type=["jpg","png"])

if uploaded_file:
    image_path = "temp_file.jpg"
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
        st.image(uploaded_file, caption="Uploaded File", use_container_width=True)
        prediction = predict(image_path)
        st.info(f"Predicted Class: {prediction}")