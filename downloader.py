import yt_dlp
import os
from pathlib import Path

def download_audio(url: str):
    """
    Downloads the best audio from a YouTube URL using yt-dlp.
    Uses cookies.txt from the project directory.
    """
    cookies_path = Path(__file__).parent.absolute() / "cookies.txt"
    uploads_dir = Path(__file__).parent.absolute() / "uploads"
    
    if not uploads_dir.exists():
        uploads_dir.mkdir(parents=True, exist_ok=True)
        
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': str(uploads_dir / '%(id)s.%(ext)s'),
        'cookiefile': str(cookies_path),
        'quiet': False,
        'no_warnings': False,
    }
    
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            return filename
    except Exception as e:
        print(f"yt-dlp error: {str(e)}")
        raise e

if __name__ == "__main__":
    # Test download
    test_url = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
    try:
        result = download_audio(test_url)
        print(f"Downloaded to: {result}")
    except Exception as e:
        print(f"Failed: {e}")
