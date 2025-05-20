# 🎨 Color Detection from Images

This is a simple and useful tool designed for designers, developers, and artists who often need to detect colors from images. You can upload an image, click anywhere on it, and instantly get the name and RGB value of the color at that pixel.

## 💡 Features
- Upload any image (PNG/JPG).
- Click on any part to detect the color.
- View color name and its RGB value.
- Visual preview of the detected color.
- Simple, clean interface built with Streamlit and OpenCV.

## 📁 Dataset
We use a `colors.csv` file containing basic color names along with RGB and hex values. You can extend it with more entries if needed.

## 🚀 Getting Started

```bash
git clone https://github.com/yourusername/color-detector
cd color-detector
pip install -r requirements.txt
streamlit run app.py
