from PIL import Image
import glob
import os
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def unpixel_image(read_dir_path, create_dir_path, new_resolution_width, base_name):
    print("unpixeling now...")
    os.makedirs(create_dir_path, exist_ok=True)
    files = sorted(glob.glob(f"./{read_dir_path}/*"), key=natural_keys)
    n = 0
    for file in files:
        img = Image.open(file)
        width, height = img.size
        img_resize = img.resize(
            (new_resolution_width, int(height*new_resolution_width/width)))
        img_resize.save(f'{create_dir_path}/{base_name}_{n}.jpg')
        print(f'{int((n+1)/len(files)*100)}% was converted')
        n += 1
