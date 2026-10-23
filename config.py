from pathlib import path
BASE_DIR=Path(__file__).resolve().parent
MODEL_DIR=BASE_DIR/"MODELS"
MODEL_PATH=MODEL_DIR/"audio_model.keras"
SAMPLE_RATE=16000
AUDIO_DURATION_SECONDS=5
LABELS={"Real","Fake)
