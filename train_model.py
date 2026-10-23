 from pathlib import Path
DATASET_DIR=Path("dataset")
MODEL_DIR=Path("models")
def check_dataset():
  if not DATASET_DIR.exists():
    print("dataset foder is missing.")
    print("create dataset/real and dataset/fake folders")
    print("Add genuine audio to real and spoofed audio to fake")
    real_dir=DATASET-DIR/"real"
    fake_dir=DATASET-DIR/"fake"
    real_files=list(real_dir.glob("*.wav")) if real_dir.exists() else[]
    fake_files=list(real_dir.glob("*.wav")) if fake_dir.exists() else[]
    print
print("Tensorflow version:",tf.__version__)
print("Model folder ready:",MODEL_DIR.resolve())
print("Next:load your dataset and train your audio classifier.")
