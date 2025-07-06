# GPy Background Remover 🖼️

A simple GUI-based tool to remove backgrounds from images using the `rembg` Python library.

## 📝 Description

This application allows you to easily remove the background from image files (supports JPG, PNG, WEBP, BMP) with just a few clicks. Powered by the `rembg` library, it provides accurate and fast background removal and saves the resulting image as a PNG file with transparency.

## 📁 Features

- Simple graphical interface using `tkinter`
- Supports multiple image formats
- Automatically saves output with transparent background
- User-friendly error handling and success messages 

## 🛠 Requirements

Before running the tool, ensure you have the following installed:

1. Python 3.x
2. Install required packages:
   ```bash
   pip install rembg onnxruntime Pillow
   ```
3. Optional: [Visual C++ Redistributable for Visual Studio](https://aka.ms/vs/17/release/vc_redist.x64.exe) (required for ONNX runtime on Windows)

> ✅ This tool works best on Windows, but can also be used on macOS or Linux with appropriate dependencies.

## ▶️ How to Run

1. Clone or download the project folder.
2. Navigate to the directory containing the script.
3. Run the script (or just click on it):
   ```bash
   python Gpy_background_remover.py
   ```
4. Select an image file using the file dialog.
5. The processed image will be saved in the same directory with `_nobg.png` appended to the original filename.

## 💡 Example

Input: `photo.jpg`  
Output: `photo_nobg.png`

## 📎 Code Overview

The script uses:
- `rembg` – for background removal
- `PIL.Image` – to open and save image files
- `tkinter` – for the GUI and file selection dialog


2025 [ivan deus]
