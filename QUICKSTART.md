# Quick Setup Guide

Follow these steps to get your transcription server running:

## 1. Install FFmpeg

**Windows (using Chocolatey):**
```bash
choco install ffmpeg
```

**Or download from:** https://ffmpeg.org/download.html

**Mac:**
```bash
brew install ffmpeg
```

**Linux:**
```bash
sudo apt install ffmpeg
```

## 2. Create Virtual Environment

```bash
python -m venv .venv
```

**Activate it:**
- Windows: `.venv\Scripts\activate`
- Mac/Linux: `source .venv/bin/activate`

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 4. Export YouTube Cookies

**CRITICAL STEP - Don't skip this!**

1. Install browser extension "Get cookies.txt LOCALLY" 
2. Go to youtube.com (make sure you're logged in)
3. Click extension icon → Export
4. Save as `cookies.txt` in this folder

## 5. Test the Setup

```bash
python verify_download.py
```

You should see: `✓ SUCCESS! Downloaded to: uploads/...`

## 6. Start the Server

**Windows:**
```bash
start.bat
```

**Mac/Linux:**
```bash
chmod +x start.sh
./start.sh
```

**Or manually:**
```bash
python main.py
```

## 7. Test It!

Open browser: http://127.0.0.1:8000/docs

Try the `/transcribe` endpoint with:
```json
{
  "url": "https://www.youtube.com/watch?v=HuFCuR1t5eU",
  "language": "en",
  "task": "transcribe"
}
```

## Troubleshooting

**403 Error?**
- Update yt-dlp: `pip install -U yt-dlp`
- Export fresh cookies.txt

**FFmpeg not found?**
- Install FFmpeg (see step 1)
- Restart your terminal after installing

**Cookies error?**
- Make sure Chrome is fully closed when running
- Or use cookies.txt file (recommended)

---

Need help? Check the full README.md for detailed documentation.
