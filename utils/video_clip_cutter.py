from moviepy.editor import VideoFileClip
import random
import string
import os

def cut_clip(input_path, start_time, end_time, output_path):
    clip = VideoFileClip(input_path).subclip(start_time, end_time)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    clip.write_videofile(output_path, codec='libx264')
    clip.close()
    print(f"Saved clip: {output_path}")




def random_code(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))


list_of_numbers = []
def number_code():
    running = True
    num = 1
    while running:
        if num in list_of_numbers:
            num += 1
        else:
            list_of_numbers.append(num)
            break

    return str(num)+'_'

full_video_path = "lv_0_20250630010300.mp4"

# List of clips to cut [(start_time, end_time, output_filename)]
clips = [
    ("00:00:02", "00:00:05", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:07", "00:00:09", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:11", "00:00:16", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:18", "00:00:22", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:23", "00:00:26", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:27", "00:00:31", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:32", "00:00:35", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:36", "00:00:40", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:41", "00:00:43", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:44", "00:00:45", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:45", "00:00:48", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:49", "00:00:52", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:53", "00:00:54", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:00:58", "00:01:00", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:01:03", "00:01:06", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:01:08", "00:01:14", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:01:15", "00:01:17", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:01:18", "00:01:20", f"clips/{number_code()}{random_code(6)}.mp4"),
    ("00:01:22", "00:01:24", f"clips/{number_code()}{random_code(6)}.mp4")
]



for start, end, out_file in clips:
    cut_clip(full_video_path, start, end, out_file)


print("Done!!!")

