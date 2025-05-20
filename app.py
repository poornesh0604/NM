
import streamlit as st
import pandas as pd
import cv2
import numpy as np
from utils import get_color_name
from PIL import Image

# Title of the app
st.set_page_config(page_title="Color Detection App")
st.title("🎨 Color Detection from Images")

# Load the color dataset
try:
    color_data = pd.read_csv("colors.csv")
except FileNotFoundError:
    st.error("colors.csv file not found. Please make sure it's in the project folder.")
    st.stop()

# Image uploader
uploaded_file = st.file_uploader("Upload an image (JPG/PNG)", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    img_array = np.array(img)

    st.image(img, caption="Uploaded Image", use_column_width=True)

    st.markdown("Click on the image to get color information (RGB + Name)")

    # Get coordinates using Streamlit's image click function
    clicked = st.image(img_array, use_column_width=True)
    st.write("Note: Interactive pixel click is not supported directly in Streamlit. Use the OpenCV window below.")

    if st.button("Open Image in Color Detection Mode (Local Only)"):
        img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)
        clicked = False

        def show_color(event, x, y, flags, param):
            if event == cv2.EVENT_LBUTTONDOWN:
                b, g, r = img_bgr[y, x]
                color_name = get_color_name(r, g, b, color_data)
                text = f"{color_name}  R={r} G={g} B={b}"
                print(text)
                cv2.rectangle(img_bgr, (20, 20), (600, 60), (b, g, r), -1)
                cv2.putText(img_bgr, text, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        
        cv2.namedWindow('Color Detection')
        cv2.setMouseCallback('Color Detection', show_color)

        while True:
            cv2.imshow('Color Detection', img_bgr)
            if cv2.waitKey(20) & 0xFF == 27:  # Press ESC to exit
                break
        cv2.destroyAllWindows()
