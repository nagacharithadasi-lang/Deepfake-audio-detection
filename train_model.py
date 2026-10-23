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
    print("Genuine WAV files:",len(real_files))
   print("spoofed WAV files:",len(fake_files))
if not real_files or not fake_files:
 print("Both classes need labeled audio before training.")
return False
print("Dataset check passed.A training pipeline is still required.")
return True
if __name__=="__main__":
 check_dataset()

