# Driving Scene Video Q&A System

Vision-Language Model for interactive Q&A on driving scenes using BLIP-VQA.

## Features
- Extract frames from dashcam videos
- Ask natural language questions about driving scenes
- Safety analysis (weather, hazards, vehicles)
- Interactive Streamlit UI

## Setup
```bash
# Clone repository
git clone https://github.com/pranavi77/driving-scene-vqa.git
cd driving-scene-vqa

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Usage

1. Extract frames from video:
```bash
python extract_frames.py
```

2. Run Streamlit app:
```bash
streamlit run app.py
```

## Sample Questions
- "What is the weather condition?"
- "Is it safe to drive?"
- "What vehicles are visible?"
- "What hazards are present?"
