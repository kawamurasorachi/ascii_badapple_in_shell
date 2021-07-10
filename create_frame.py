import cv2
import os


def save_all_frames(video_path, fps, dir_path, basename, ext='jpg'):
    print("generate frame now...")
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))
    video_fps = cap.get(cv2.CAP_PROP_FPS)
    result_fps = video_fps / fps

    n = 0

    while 1+result_fps*n <= int(cap.get(cv2.CAP_PROP_FRAME_COUNT)):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 1+result_fps*n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(
                base_path, str(n).zfill(digit), ext), frame)
            print(
                f'{int((1+result_fps*n)/int(cap.get(cv2.CAP_PROP_FRAME_COUNT))*100)}% was converted')
            n += 1
        else:
            return
