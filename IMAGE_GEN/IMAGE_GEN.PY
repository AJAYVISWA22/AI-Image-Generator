import streamlit as st
import requests
from PIL import Image
import io

st.title('AI Image Generation')

API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3-medium-diffusers"
headers = {"Authorization": "Bearer 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"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        st.error(f"Failed to fetch image. Status code: {response.status_code}")
        return None

prompt = st.text_input('Enter Your prompt')

if st.button('Generate'):
    if prompt:
        image_bytes = query({"inputs": prompt})
        if image_bytes:
            try:
                image = Image.open(io.BytesIO(image_bytes))
                st.image(image, caption="Generated Image")
            except IOError:
                st.error("Failed to open the image. The response might not contain valid image data.")
        else:
            st.error("No image data received from the API.")
    else:
        st.error("Please enter a prompt.")
