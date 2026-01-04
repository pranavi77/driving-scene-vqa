import cv2
import os
from pathlib import Path

def extract_frames(video_path, output_folder="frames", frame_interval=30):
    """
    Extract frames from video at regular intervals
    
    Args:
        video_path: Path to video file
        output_folder: Where to save frames
        frame_interval: Save every Nth frame (30 = ~1 frame per second for 30fps video)
    """
    
    Path(output_folder).mkdir(parents=True, exist_ok=True)
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        print(f"Error: Could not open video {video_path}")
        return
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    duration = total_frames / fps
    
    print(f"Video info:")
    print(f"FPS: {fps}")
    print(f"Total frames: {total_frames}")
    print(f"Duration: {duration:.2f} seconds")
    print(f"Extracting every {frame_interval} frames...")
    
    frame_count = 0
    saved_count = 0
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        if frame_count % frame_interval == 0:
            timestamp = frame_count / fps
            output_path = f"{output_folder}/frame_{saved_count:04d}_t{timestamp:.2f}s.jpg"
            cv2.imwrite(output_path, frame)
            saved_count += 1
            if saved_count % 10 == 0:
                print(f"  Extracted {saved_count} frames...")
        
        frame_count += 1
    
    cap.release()
    print(f"\nDone! Extracted {saved_count} frames to '{output_folder}/'")
    print(f"Average: 1 frame every {duration/saved_count:.2f} seconds")

if __name__ == "__main__":
    # Example usage
    video_path = "videos/dashcam.webm"  
    extract_frames(video_path, output_folder="frames", frame_interval=30)