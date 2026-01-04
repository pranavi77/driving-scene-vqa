import streamlit as st
from PIL import Image
import os
from video_qa import VideoQA

st.set_page_config(page_title="Driving Scene VQA", layout="wide")

# Initialize model (cached)
@st.cache_resource
def load_model():
    return VideoQA()

st.title("🚗 Driving Scene Video Q&A")
st.markdown("Ask questions about driving scenes from video frames")

# Load model
with st.spinner("Loading model..."):
    vqa = load_model()

# Get list of frames
frames_dir = "frames"
if os.path.exists(frames_dir):
    frames = sorted([f for f in os.listdir(frames_dir) if f.endswith('.jpg')])
    
    if frames:
        # Sidebar: Frame selector
        st.sidebar.header("Select Frame")
        frame_idx = st.sidebar.slider("Frame number", 0, len(frames)-1, 0)
        selected_frame = frames[frame_idx]
        
        # Display frame
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.subheader("Video Frame")
            image_path = os.path.join(frames_dir, selected_frame)
            image = Image.open(image_path)
            st.image(image, use_container_width=True)
            st.caption(selected_frame)
        
        with col2:
            st.subheader("Ask Questions")
            
            # Predefined questions
            preset_questions = [
                "What is the weather condition?",
                "Is it safe to drive?",
                "What vehicles are visible?",
                "What hazards are present?",
                "What should the driver do?"
            ]
            
            selected_preset = st.selectbox("Choose a question:", ["Custom"] + preset_questions)
            
            if selected_preset == "Custom":
                question = st.text_input("Enter your question:")
            else:
                question = selected_preset
            
            if st.button("Get Answer", type="primary"):
                if question:
                    with st.spinner("Analyzing..."):
                        answer = vqa.ask_question(image_path, question)
                        st.success(f"**Answer:** {answer}")
                else:
                    st.warning("Please enter a question")
            
            # Quick analysis
            st.markdown("---")
            if st.button("Quick Safety Analysis"):
                with st.spinner("Analyzing safety..."):
                    questions = [
                        ("Weather", "What is the weather condition?"),
                        ("Safety", "Is it safe to drive?"),
                        ("Vehicles", "What vehicles are visible?"),
                        ("Hazards", "What hazards are present?")
                    ]
                    
                    for label, q in questions:
                        answer = vqa.ask_question(image_path, q)
                        st.write(f"**{label}:** {answer}")
    else:
        st.warning("No frames found. Run extract_frames.py first.")
else:
    st.error("Frames directory not found. Run extract_frames.py first.")