# 🎥 YouTube Transcriber

A Streamlit app that extracts YouTube video transcripts and generates **detailed, structured summaries** using **Google’s Gemini API**.

---

## Tech Stack

- Python, Streamlit  
- youtube_transcript_api  
- Google Generative AI (Gemini)  
- python-dotenv  

---

##  How It Works

1. **User inputs a YouTube URL**
2. **Transcript fetched** using `youtube_transcript_api` (translated if needed)
3. **Gemini generates summary** with:
   - Introduction  
   - Subtopics  
   - Sentence Analysis  
   - Key Concepts  
   - Real-World Use  
   - Conclusion

✅ Handles missing/translated transcripts  
✅ Graceful error handling  

---

## Run Locally

```bash
git clone https://github.com/nikhilmangali1/yt_transcriber.git
cd YT_TRANSCRIBER
pip install -r requirements.txt
echo "GOOGLE_API_KEY=your-key" > .env
streamlit run app.py
```
##  Project Structure

```
YT_TRANSCRIBER/
├── app.py
├── .env
├── requirements.txt
├── .gitignore
```


###  Use Cases
Students – lecture summaries

Professionals – meeting notes

Researchers – talk/webinar overviews

  
