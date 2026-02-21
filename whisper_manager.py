import whisper
import os

class WhisperManager:
    def __init__(self, model_size="base"):
        print(f"Loading Whisper model: {model_size}...")
        self.model = whisper.load_model(model_size)
    
    def transcribe(self, audio_path: str, language: str = None, task: str = "transcribe"):
        """
        Transcribes the given audio file using Whisper.
        """
        if not os.path.exists(audio_path):
            raise FileNotFoundError(f"Audio file not found: {audio_path}")
            
        print(f"Transcribing {audio_path} (language={language}, task={task})...")
        
        options = {
            "task": task,
        }
        if language:
            options["language"] = language
            
        result = self.model.transcribe(audio_path, **options)
        return result

# Singleton instance
whisper_instance = WhisperManager()
