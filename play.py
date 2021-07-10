import glob
import time
import re


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    return [atoi(c) for c in re.split(r'(\d+)', text)]


def play_badapple(read_dir_path, fps):
    files = sorted(glob.glob(f"./{read_dir_path}/*"), key=natural_keys)
    play_data = []
    for file in files:
        with open(file, 'r') as f:
            data = f.read()
            play_data.append(data)
    for i in play_data:
        print(i)
        time.sleep(1/fps)
