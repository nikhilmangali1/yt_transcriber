import streamlit as st  # type: ignore
from dotenv import load_dotenv  # type: ignore
import os
import google.generativeai as genai  # type: ignore
from youtube_transcript_api import YouTubeTranscriptApi  # type: ignore

# Load environment variables
load_dotenv()

# Configure API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


# models = genai.list_models()
# for m in models:
#     print(m.name, m.supported_generation_methods)

# Define the prompt
prompt = """
You are an expert YouTube video summarizer. Your task is to analyze the transcript and provide a highly detailed, comprehensive report IN ENGLISH ONLY. Regardless of the input language, your summary must be in English. The report should cover every element of the transcript thoroughly and explain each sentence broadly. Include examples where appropriate, and structure your report as follows:

Introduction: Provide a detailed overview of the video's overall topic, including any relevant background information or context.
Main Content: Explain each section or segment of the video with subheadings. Describe the information in full, capturing all nuances, background concepts, and details conveyed by the speaker.
In-Depth Analysis:
For each main idea, break down individual sentences or phrases, explaining the meaning, significance, and any technical details or jargon used.
Provide examples or comparisons where necessary to clarify complex points.
Key Insights and Concepts:
Highlight and elaborate on any critical facts, key concepts, or theories mentioned.
Include additional context to make complex ideas accessible, such as explaining the historical or practical relevance of specific points.
Real-World Applications and Examples: Identify and describe any practical applications or examples in depth. Explain how these applications are relevant to the topic and their significance in real-world settings.
Conclusion: Summarize the core takeaway of the video in a few detailed sentences, reflecting the video’s main argument or purpose.
IMPORTANT: THE ENTIRE SUMMARY MUST BE IN ENGLISH ONLY.

There is no word limit for this summary, so include all necessary details to provide a complete understanding of the video content.
"""

# Extract transcript details (no translation)
def extract_transcript_details(youtube_video_url):
    try:
        video_id = youtube_video_url.split("v=")[1].split("&")[0]
        transcript_list = YouTubeTranscriptApi.list_transcripts(video_id)

        # Get first available transcript regardless of language
        transcript = next(iter(transcript_list))
        transcript_data = transcript.fetch()

        # ✅ FIXED LINE
        transcript_text = " ".join([i.text for i in transcript_data])
        return transcript_text

    except Exception as e:
        st.error(f"Transcript extraction failed: {e}")
        return None

# Generate Gemini summary
def generate_gemini_content(transcript_text, prompt):
    try:
        model = genai.GenerativeModel(model_name="gemini-1.5-flash-latest")
        response = model.generate_content(f"{prompt}\nTranscript:\n{transcript_text}")
        return response.text
    except Exception as e:
        st.error(f"Error generating content: {e}")
        return None

# Streamlit UI
st.title("YouTube Transcript to Detailed Notes Converter")
youtube_link = st.text_input("Enter YouTube Video Link:")

if youtube_link:
    try:
        video_id = youtube_link.split("v=")[1].split("&")[0]
        st.image(f"http://img.youtube.com/vi/{video_id}/0.jpg", use_column_width=True)
    except:
        st.warning("Invalid YouTube URL")

if st.button("Get Detailed Notes"):
    transcript_text = extract_transcript_details(youtube_link)

    if transcript_text:
        st.success("Transcript extracted successfully!")
        summary = generate_gemini_content(transcript_text, prompt)
        if summary:
            st.write(summary)
        else:
            st.error("Failed to generate summary.")
    else:
        st.error("Transcript extraction failed.")
