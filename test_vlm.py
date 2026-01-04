from transformers import pipeline
from PIL import Image
import os

# Initialize VLM (using BLIP-2 for now - simpler than LLaVA)
print("Loading model... (this will take a minute)")
vlm = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")

# Test on first frame
frame_path = "frames/frame_0020_t20.00s.jpg"

if os.path.exists(frame_path):
    image = Image.open(frame_path)
    
    # Generate description
    result = vlm(image)
    print(f"\nFrame: {frame_path}")
    print(f"Description: {result[0]['generated_text']}")
else:
    print(f"Frame not found: {frame_path}")