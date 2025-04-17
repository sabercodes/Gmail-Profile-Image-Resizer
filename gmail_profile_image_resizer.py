import os
import face_recognition
from PIL import Image

def crop_face_and_resize(input_folder, output_folder, size=(300, 300), margin=120):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            image_path = os.path.join(input_folder, filename)
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)

            if face_locations:
                top, right, bottom, left = face_locations[0]

                # تعديل المارجن علشان يدي مساحة أكبر حوالين الراس، خاصة من فوق
                margin_top = int(margin * 1.8)     # مساحة أكبر من فوق
                margin_sides = int(margin * 1.2)   # مساحة أفقية أكبر
                margin_bottom = int(margin * 0.8)  # مساحة أقل تحت

                new_top = max(0, top - margin_top)
                new_right = min(image.shape[1], right + margin_sides)
                new_bottom = min(image.shape[0], bottom + margin_bottom)
                new_left = max(0, left - margin_sides)

                face_image = image[new_top:new_bottom, new_left:new_right]
                pil_image = Image.fromarray(face_image)
                pil_image = pil_image.resize(size, Image.Resampling.LANCZOS)

                output_path = os.path.join(output_folder, filename)
                pil_image.save(output_path)
                print(f"Saved: {output_path}")
            else:
                print(f"No face found in {filename}")

# ✨ تعديل مهم: غير المسارات حسب جهازك أو شغّل السكربت من نفس المجلد اللي فيه input_images و gmail_ready_images
crop_face_and_resize("input_images", "gmail_ready_images")
