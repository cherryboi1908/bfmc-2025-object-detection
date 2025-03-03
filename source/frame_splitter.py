import os 
import cv2
import numpy as np

def split_video_into_frames(video_path, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    # Open the video file
    cap = cv2.VideoCapture(video_path)
    # Check if the video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    # Read the video frame by frame and save each frame as an image file
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps)  # Save 1 frame per second
    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        # Save the frame as an image file
        if frame_count % frame_interval == 0:
            frame_path = os.path.join(output_folder, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_path, frame)
            print(f"Saved frame {frame_count//frame_interval}")
        
        frame_count += 1
            
    # Release the video capture object
    cap.release()
    print("Video frames saved successfully.")
    return frame_count

for i in range(12):
    output_folder = f'D:\pleizsonoob\Others\\bfmc\dataset\\frame_saved\\vid_{i+1}'
    video_path = "D:\pleizsonoob\Others\\bfmc\\dataset\\videos"
    video_files = os.listdir(video_path)
    video_file_path = os.path.join(video_path, video_files[i])
    split_video_into_frames(video_file_path, output_folder)
    print(f"Video {i+1} frames saved successfully.")