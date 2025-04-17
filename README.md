# Gmail Profile Image Resizer

This is a simple Python script that detects faces in images, adds extra space to include the full head (including hair), crops the image, and resizes it to 300x300 pixels. This is especially useful for Gmail or any profile image requirements.

To use this script, you need Python 3.9 and some required libraries.

First, make sure Python is installed on your computer. Then, follow these steps:

1. Clone or download this repository.

2. (Optional but recommended) Create a virtual environment by running:  
python -m venv faceenv  
Activate it with:  
faceenv\Scripts\activate  (for Windows)

3. Install the required libraries:  
pip install face_recognition Pillow

4. Place your original images inside a folder named "input_images" in the same directory as the script.

5. Run the script:  
python gmail_profile_image_resizer.py

6. The processed images will be saved automatically inside a folder called "gmail_ready_images".

Folder structure should look like this:  
gmail-profile-image-resizer/  
├── gmail_profile_image_resizer.py  
├── README.md  
├── input_images/  
└── gmail_ready_images/

What the script does:  
- Detects the face in the image  
- Adds margin around the face so the full head and hair are visible  
- Crops and resizes the image to 300x300  
- Saves it in the output folder

If you face issues installing dlib, try upgrading pip or use precompiled wheels.

This script uses the face_recognition library powered by dlib, and Pillow for image resizing.

Need help? Open an issue on the repository.
