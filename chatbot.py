from transformers import pipeline
import gradio as gr

# Load AI Model
chatbot = pipeline("text-generation", model="microsoft/DialoGPT-medium")

# Define chatbot function
def chat_with_ai(user_input):
    response = chatbot(user_input, max_length=100)
    return response[0]['generated_text']

# Create Web UI
iface = gr.Interface(fn=chat_with_ai, inputs="text", outputs="text")
iface.launch()