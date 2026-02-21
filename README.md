<<<<<<< HEAD
# YouTube Transcription API

FastAPI backend that downloads YouTube videos and transcribes them using OpenAI's Whisper model.

## Features

- Download audio from YouTube URLs using yt-dlp
- Transcribe audio using Whisper AI
- Support for multiple languages
- RESTful API with automatic documentation

## Requirements

- Python 3.8+
- FFmpeg (for audio processing)
- Chrome or Firefox browser (to export cookies)

## Setup Instructions

### 1. Install FFmpeg

**Windows:**
```bash
# Using chocolatey
choco install ffmpeg

# Or download from: https://ffmpeg.org/download.html
```

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt update
sudo apt install ffmpeg
```

### 2. Install Python Dependencies

```bash
# Create virtual environment (recommended)
python -m venv .venv

# Activate virtual environment
# Windows:
.venv\Scripts\activate
# Mac/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Export YouTube Cookies

YouTube requires authentication cookies to download videos. Here's how to export them:

**Step 1:** Install browser extension
- Chrome: Install "Get cookies.txt LOCALLY" extension
- Firefox: Install "cookies.txt" extension

**Step 2:** Export cookies
1. Go to `youtube.com` and make sure you're logged in
2. Click the extension icon
3. Click "Export" or "Download"
4. Save the file as `cookies.txt` in the project root directory

**Important:** The cookies.txt file must be in the same directory as your Python files!

### 4. Verify Setup

Test that everything works:

```bash
python verify_download.py
```

If successful, you should see:
```
✓ cookies.txt found
✓ downloader module imported
✓ SUCCESS! Downloaded to: uploads/...
```

## Running the Server

```bash
# Start the server
python main.py

# Or use uvicorn directly
uvicorn main:app --reload
```

Server will start at: `http://127.0.0.1:8000`

## API Documentation

Once running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## API Usage

### Transcribe a YouTube Video

**Endpoint:** `POST /transcribe`

**Request Body:**
```json
{
  "url": "https://www.youtube.com/watch?v=VIDEO_ID",
  "language": "en",
  "task": "transcribe"
}
```

**Parameters:**
- `url` (required): YouTube video URL
- `language` (optional): Language code (default: "en")
  - Examples: "en", "es", "fr", "de", "ja", "zh"
- `task` (optional): "transcribe" or "translate" (default: "transcribe")
  - "transcribe": Transcribe in original language
  - "translate": Transcribe and translate to English

**Response:**
```json
{
  "job_id": "uuid",
  "status": "completed",
  "text": "Full transcription text...",
  "segments": [
    {
      "start": 0.0,
      "end": 5.2,
      "text": "First segment..."
    }
  ],
  "language": "en",
  "duration": 120.5,
  "processing_time_seconds": 45.2
}
```

### Example with cURL

```bash
curl -X POST "http://127.0.0.1:8000/transcribe" \
  -H "Content-Type: application/json" \
  -d '{
    "url": "https://www.youtube.com/watch?v=HuFCuR1t5eU",
    "language": "en",
    "task": "transcribe"
  }'
```

## Troubleshooting

### Error: HTTP 403 Forbidden

**Cause:** YouTube is blocking the download request

**Solutions:**
1. Update yt-dlp: `pip install -U yt-dlp`
2. Export fresh cookies.txt from your browser
3. Make sure you're logged into YouTube when exporting cookies

### Error: Could not copy Chrome cookie database

**Cause:** Chrome is running and locking the cookie file

**Solution:** Use cookies.txt file instead (see Setup Instructions #3)

### Error: FFmpeg not found

**Cause:** FFmpeg is not installed or not in PATH

**Solution:** Install FFmpeg (see Setup Instructions #1)

### Error: Cookies.txt not found

**Cause:** The cookies.txt file is missing

**Solution:** Export cookies from your browser (see Setup Instructions #3)

## File Structure

```
project/
├── main.py                 # FastAPI server
├── downloader.py          # YouTube download logic
├── whisper_manager.py     # Whisper transcription
├── requirements.txt       # Python dependencies
├── verify_download.py     # Test script
├── cookies.txt           # YouTube cookies (you create this)
├── uploads/              # Downloaded audio files (auto-created)
└── README.md             # This file
```

## Notes

- First transcription takes longer (Whisper model loads on first request)
- Subsequent transcriptions are faster (model stays in memory)
- Long videos (30+ minutes) may take 5-10 minutes to process on CPU
- Downloaded audio files are saved in `uploads/` directory
- The server runs on CPU by default (GPU support requires additional setup)

## License

MIT License - See LICENSE file for details
=======
# youtube-transcription-api
AI-powered YouTube video transcription using Whisper AI
>>>>>>> ca8bf5e0a16e058980692937b637dd7684adc183
