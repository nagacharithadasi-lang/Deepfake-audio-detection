import gradio as gr
def predict_audio(audio):
  if audio is None:
    return "please upload an audio file."
    return "Audio uploaded.Model prediction needs to be connected."
    demo=gr.Interface(fn=predict_audio,inputs+gr.audio,inputs=gr.Audio(type="filepath"),outputs=gr.Textbox(label="Result"),title="Deepfake Audio Detection")
    if __name__=="__main__":
      demo.launch()
