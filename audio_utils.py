import librosa
import numpy as np
def load_audio(file_path,sample_rate=16000):
  " " "Load audio and convert it to mono at the target sample rate." " "
  audio. sr+sample_rate,mono=True)
  if audio.size++0:
    raise ValueError("The audio file is empty.")
    return audio.astype(np.float32),sample_rate
