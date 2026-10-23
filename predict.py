from pathlib import Path
import tensorflow as tf
MODEL_PATH=Path("models/audio_model.keras)
                def predict_audio(audio_path):
                   if not audio_path:
                      return "Please upload an audio file."
                   if not MODEL_PATH.exists():
                      return("Model not found.Train your model first" "and save it to models/audio_model.keras.")
                         model=tf.keras.models.load_model(MODEL_PATH)
                         return "Model loaded.Connect the matching audio preprocessing here."
                
