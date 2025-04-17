# Gmail Profile Image Resizer

A simple script using `face_recognition` and `Pillow` to crop faces from images and prepare them for Gmail profile pictures. It ensures the full head (including hair) is visible, not just a close-up on the face.

---

## 🔧 Tools & Libraries Used

- Python 3.9
- [face_recognition](https://github.com/ageitgey/face_recognition)
- [dlib](https://github.com/davisking/dlib)
- [Pillow (PIL)](https://python-pillow.org)
- Optional: `virtualenv` for isolated environment

---

## ⚙️ How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/sabercodes/gmail-profile-image-resizer.git
cd gmail-profile-image-resizer

2. (Optional) Create and Activate Virtual Environment
python -m venv faceenv
faceenv\Scripts\activate

