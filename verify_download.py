import os
from pathlib import Path
from downloader import download_audio

def verify():
    print("--- YouTube Download Verification ---")
    
    # 1. Check for cookies.txt
    cookies_path = Path(__file__).parent.absolute() / "cookies.txt"
    if not cookies_path.exists():
        print(f"WARNING: cookies.txt not found at {cookies_path}")
        print("Downloads might fail if video is age-restricted or requires login.")
    else:
        print(f"SUCCESS: Found cookies.txt at {cookies_path}")
        
    # 2. Test video
    test_video_id = "dQw4w9WgXcQ" # Never Gonna Give You Up
    test_url = f"https://www.youtube.com/watch?v={test_video_id}"
    
    print(f"Attempting to download: {test_url}")
    
    try:
        filename = download_audio(test_url)
        if os.path.exists(filename):
            print(f"SUCCESS: Downloaded file found at {filename}")
            print(f"File size: {os.path.getsize(filename)} bytes")
        else:
            print(f"FAILURE: download_audio returned {filename} but file does not exist.")
    except Exception as e:
        print("FAILURE: Download failed with error:")
        print("-" * 20)
        import traceback
        traceback.print_exc()
        print("-" * 20)

if __name__ == "__main__":
    verify()
