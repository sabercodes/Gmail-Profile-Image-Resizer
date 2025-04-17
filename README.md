# Gmail Profile Image Resizer

This project is a simple Python script that takes images, finds the face, and crops the image so that it includes the **full head (with hair)** — not just a close-up of the face. It's useful for preparing profile pictures, like for Gmail.

---

## 📂 What This Script Does

- Finds the face in each photo.
- Adds space around the face to include the full head.
- Resizes the photo to 300x300 pixels.
- Saves the new photo in a folder.

---

## 🛠️ What You Need

### Tools:

- Python 3.9
- Libraries:
  - `face_recognition`
  - `dlib`
  - `Pillow` (for image editing)

---

## ▶️ How to Use

### Step 1: Download the Project

If you're using GitHub, click the green “Code” button and choose **Download ZIP**  
Then extract the folder.

Or if you know Git, run:

```bash
git clone https://github.com/sabercodes/gmail-profile-image-resizer.git
