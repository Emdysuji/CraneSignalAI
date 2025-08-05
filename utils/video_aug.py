import os
import cv2
from moviepy.editor import ImageSequenceClip

import albumentations as A


# --- CONFIGURATION ---
DATASET_DIR = "Path To Your Dataset"  # <- root folder where class folders are
AUG_PER_VIDEO = 9             # how many augmented versions to create
IMG_SIZE_WIDTH = 1280
IMG_SIZE_HEIGHT = 720
FPS = 30                      # output video FPS

# --- AUGMENTATION PIPELINE ---


replayable_augs = A.ReplayCompose([
    A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=10, p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.GaussianBlur(blur_limit=3, p=0.3),
    A.MotionBlur(blur_limit=3, p=0.2),
    A.GaussNoise(var_limit=(10.0, 50.0), p=0.3),
    A.GridDistortion(num_steps=5, distort_limit=0.03, p=0.3),
    A.CoarseDropout(max_holes=4, max_height=20, max_width=20, p=0.3),
    A.HueSaturationValue(p=0.3),
    A.RGBShift(p=0.3)
])


print("🔄 Starting augmentation...")

# Loop through each class folder
for class_name in os.listdir(DATASET_DIR):
    class_path = os.path.join(DATASET_DIR, class_name)
    if not os.path.isdir(class_path):
        continue

    print(f"📂 Processing class: {class_name}")
    video_files = [f for f in os.listdir(class_path) if f.endswith(".mp4")]


    for file in video_files:
        file_path = os.path.join(class_path, file)

        # Read all frames from the video
        cap = cv2.VideoCapture(file_path)
        frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            frame = cv2.resize(frame, (IMG_SIZE_WIDTH, IMG_SIZE_HEIGHT))
            frames.append(frame)
        cap.release()

        if not frames:
            print(f"⚠️ Skipped empty or unreadable video: {file}")
            continue


        # Apply augmentations
        for i in range(AUG_PER_VIDEO):
            # Convert to RGB (albumentations uses RGB format)
            frames_rgb = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in frames]

            # Generate the replayable params on the first frame
            replay = replayable_augs(image=frames_rgb[0])["replay"]

            # Apply same augmentation to all frames
            aug_frames = [A.ReplayCompose.replay(replay, image=img)["image"] for img in frames_rgb]

            # Convert back to BGR for saving
            # aug_frames_bgr = [cv2.cvtColor(f, cv2.COLOR_RGB2BGR) for f in aug_frames]

            # Convert to RGB for MoviePy
            # rgb_frames = [cv2.cvtColor(f, cv2.COLOR_BGR2RGB) for f in aug_frames]

            out_filename = f"{os.path.splitext(file)[0]}_aug{i}.mp4"
            out_path = os.path.join(class_path, out_filename)

            # Write the new video

            clip = ImageSequenceClip(aug_frames, fps=FPS)
            clip.write_videofile(out_path, codec='libx264', audio=False, verbose=False, logger=None)

    print(f"✅ Done with class: {class_name}")

print("🎉 All videos augmented and saved in-place.")
