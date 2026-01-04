from transformers import BlipProcessor, BlipForQuestionAnswering
from PIL import Image
import torch
import os

class VideoQA:
    def __init__(self):
        print("Loading VQA model...")
        self.processor = BlipProcessor.from_pretrained("Salesforce/blip-vqa-base")
        self.model = BlipForQuestionAnswering.from_pretrained("Salesforce/blip-vqa-base")
        print("Model loaded!")
    
    def ask_question(self, image_path, question):
        """Ask a question about an image"""
        image = Image.open(image_path).convert('RGB')
        
        # Process
        inputs = self.processor(image, question, return_tensors="pt")
        
        # Generate answer
        out = self.model.generate(**inputs)
        answer = self.processor.decode(out[0], skip_special_tokens=True)
        
        return answer

# Test it
if __name__ == "__main__":
    vqa = VideoQA()
    
    # Test questions on a frame
    frame = "frames/frame_0020_t20.00s.jpg"
    
    questions = [
        "What is the weather condition?",
        "Is it safe to drive?",
        "What vehicles are visible?",
        "What hazards are present?"
    ]
    
    print(f"\nAnalyzing: {frame}\n")
    for q in questions:
        answer = vqa.ask_question(frame, q)
        print(f"Q: {q}")
        print(f"A: {answer}\n")