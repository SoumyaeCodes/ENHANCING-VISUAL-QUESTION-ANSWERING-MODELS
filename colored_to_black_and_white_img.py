import os
from PIL import Image
def convert_to_black_and_white(source_folder):
    destination_folder = "BWImg"
        if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    for filename in os.listdir(source_folder):
        file_path = os.path.join(source_folder, filename)
        if os.path.isfile(file_path) and filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            img = Image.open(file_path)
            bw_img = img.convert('L')
            save_path = os.path.join(destination_folder, filename)
            bw_img.save(save_path)
    print(f"All images have been converted and saved in {destination_folder}")