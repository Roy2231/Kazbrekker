import gradio as gr
from transformers import pipeline

# This loads the model you just pushed to GitHub
pipe = pipeline("text-generation", model="Roy2231/Kazbrekker") 

def predict(text):
    return pipe(text)[0]["generated_text"]

demo = gr.Interface(fn=predict, inputs="text", outputs="text")
demo.launch()
