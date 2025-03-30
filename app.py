1
import gradio as gr
from transformers import pipeline

chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def chat_with_ai(user_input):
    response = chatbot(user_input, max_length=100)
    return response[0]['generated_text']

iface = gr.Interface(fn=chat_with_ai, inputs="text", outputs="text")
iface.launch()
