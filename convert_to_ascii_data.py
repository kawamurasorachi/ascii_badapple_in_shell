import glob
import os
from PIL import Image
import numpy as np
import math
import time
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]



def pic_to_ascii(read_dir_path, create_dir_path, base_name):
    print("converting to ascii now...")
    ascii_data = "＠％＃＊＋＝ー：。　"
    ascii_data_length = len(ascii_data)
    os.makedirs(create_dir_path, exist_ok=True)
    files = sorted(glob.glob(f"./{read_dir_path}/*"),key=natural_keys)
    n = 0
    for file in files:
        img = Image.open(file)
        width, height = img.size
        # print(f'w:{width},h:{height}')
        with open(f"{create_dir_path}/{base_name}_{n}.txt", mode="a") as f:
            write_text = ''
            for y in range(height):
                for x in range(width):
                    r, g, b = img.getpixel((x, y))
                    g = (r + g + b)/3
                    choosen_ascii = ascii_data[math.floor(
                        (g/256)*ascii_data_length)]
                    write_text += choosen_ascii
                write_text += "\n"
            f.write(write_text)
        print(f'{int((n+1)/len(files)*100)}% was converted')
        n += 1
