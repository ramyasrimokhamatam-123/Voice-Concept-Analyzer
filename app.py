import streamlit as st
import time

from speech_to_text import speech_to_text
from semantic_similarity import semantic_similarity
from audio_features import extract_audio_features
from filler_words import filler_word_ratio
from evaluation import evaluate_understanding
from waveform import plot_waveform
from report_generator import generate_report

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyser",
    page_icon="🎤",
    layout="wide"
)

st.title("🎤 Voice Based Concept Understanding Analyser")
st.write("Upload an audio explanation and compare it with the reference answer.")

# ---------------- Session State ----------------

if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "similarity" not in st.session_state:
    st.session_state.similarity = 0.0

if "score" not in st.session_state:
    st.session_state.score = 0

if "level" not in st.session_state:
    st.session_state.level = ""

# ---------------- User Input ----------------

reference_answer = st.text_area("Enter the Reference Answer")

audio = st.file_uploader(
    "Upload an audio file",
    type=["wav", "mp3"]
)

# ---------------- Processing ----------------

if audio is not None:

    # Save uploaded file
    with open("uploads/audio.wav", "wb") as f:
        f.write(audio.getbuffer())

    st.success("✅ Audio uploaded successfully!")

    # Audio player
    st.audio(audio)

    # Start processing timer
    start_time = time.time()

    # Speech to Text
    text = speech_to_text("uploads/audio.wav")
    st.session_state.transcript = text

    st.subheader("📝 Transcribed Text")
    st.write(st.session_state.transcript)

    if reference_answer:

        # Semantic Similarity
        similarity = semantic_similarity(
            text,
            reference_answer
        )
        st.session_state.similarity = similarity

        # Audio Features
        audio_features = extract_audio_features(
            "uploads/audio.wav"
        )

        # Filler Word Ratio
        filler_ratio = filler_word_ratio(text)

        # Final Evaluation
        score, level, color = evaluate_understanding(
            similarity,
            filler_ratio,
            audio_features
        )

        st.session_state.score = score
        st.session_state.level = level

        st.markdown("---")
        st.subheader("📊 Evaluation Results")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Semantic Similarity",
                f"{similarity:.2f}%"
            )

        with col2:
            st.metric(
                "Filler Word Ratio",
                f"{filler_ratio:.2%}"
            )

        with col3:
            st.metric(
                "Final Score",
                score
            )

        st.subheader("🎧 Audio Features")
        st.write(audio_features)

        # Waveform
        st.subheader("📈 Audio Waveform")
        waveform_image = plot_waveform("uploads/audio.wav")
        st.image(waveform_image, width="stretch")

        # Understanding Level
        st.subheader("🏆 Understanding Level")
        st.markdown(
            f"<h2 style='color:{color}'>{level}</h2>",
            unsafe_allow_html=True
        )

        # Generate PDF
        pdf_file = generate_report(
            text,
            similarity,
            filler_ratio,
            score,
            level
        )

        st.subheader("📄 Report")

        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download PDF Report",
                data=file,
                file_name="Voice_Analysis_Report.pdf",
                mime="application/pdf"
            )

        # Processing Time
        end_time = time.time()

        st.subheader("⏱ Processing Time")
        st.write(f"{end_time - start_time:.2f} seconds")

    else:
        st.warning("⚠ Please enter the reference answer.")

else:
    st.info("Please upload an audio file to begin.")