# 📸 Gmail Profile Image Resizer

This project is a simple Python script that takes images, detects the face, and crops them with extra space to include the full head (not just a close-up of the face). The images are then resized to 300x300 pixels — perfect for Gmail or other profile pictures.

---

## ✅ What This Script Does

- Finds the face in each image.
- Adds extra margin around the face (so the full head and hair show).
- Resizes the image to 300x300 pixels.
- Saves the processed images in a separate folder.

---

## 🧰 Requirements

Make sure you have these installed:

- Python 3.9
- Required Python packages:
  - `face_recognition`
  - `dlib`
  - `Pillow`

> ⚠️ Installing `dlib` might be tricky. You’ll find help in the error message or can ask for support.

---

## 📝 How to Use

### 📥 Step 1: Download or Clone the Project

Download the ZIP or use Git:

```bash
git clone https://github.com/sabercodes/gmail-profile-image-resizer.git
