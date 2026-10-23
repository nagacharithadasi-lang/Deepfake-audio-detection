from pathlib import Path
import tensorflow as tf
MODEL_DIR=Path("models")
MODEL_DIR.mkdir(exist_ok=True)
print("Tensorflow version:",tf.__version__)
print("Model folder ready:",MODEL_DIR.resolve())
print("Next:load your dataset and train your audio classifier.")
