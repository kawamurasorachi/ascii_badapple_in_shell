import create_frame
import unpixel_frame
import convert_to_ascii_data
import play

# -------------------------
# Change Params
create_frame_dir = './data'
unpixel_frame_dir = './data2'
convert_ascii_dir = './data3'
mov_file_name = 'Bad Apple!!.mp4'
fps = 20  # max 32
resolution_width = 60
# -------------------------

create_frame.save_all_frames(
    mov_file_name, fps, create_frame_dir, 'frame')
unpixel_frame.unpixel_image(
    create_frame_dir, unpixel_frame_dir, resolution_width, 'frame_unpixel')
convert_to_ascii_data.pic_to_ascii(
    unpixel_frame_dir, convert_ascii_dir, 'frame_ascii')
play.play_badapple(convert_ascii_dir, fps)
