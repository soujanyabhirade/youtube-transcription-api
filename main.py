from fastapi import FastAPI, HTTPException, Body
from fastapi.middleware.cors import CORSMiddleware
import traceback
import os
from downloader import download_audio
from whisper_manager import whisper_instance
from pydantic import BaseModel
from typing import Optional

app = FastAPI(title="YouTube Transcription API")

# Enable CORS for localhost:3000
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TranscribeRequest(BaseModel):
    url: str
    language: Optional[str] = None
    task: Optional[str] = "transcribe"

@app.post("/transcribe")
async def transcribe_video(request: TranscribeRequest):
    try:
        # 1. Download audio
        print(f"Starting download for: {request.url}")
        audio_path = download_audio(request.url)
        
        # 2. Transcribe
        print(f"Starting transcription for: {audio_path}")
        result = whisper_instance.transcribe(
            audio_path, 
            language=request.language, 
            task=request.task
        )
        
        # 3. Clean up (optional, keeping for now as per uploads/ requirement)
        # os.remove(audio_path)
        
        return {
            "status": "success",
            "text": result["text"],
            "segments": result.get("segments", []),
            "language": result.get("language", "en")
        }
        
    except Exception as e:
        error_traceback = traceback.format_exc()
        print(f"Error in /transcribe: {error_traceback}")
        raise HTTPException(status_code=500, detail={
            "error": str(e),
            "traceback": error_traceback
        })

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
