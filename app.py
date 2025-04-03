#import all the libs
import gradio as gr
import ollama
import os
from dotenv import load_dotenv

# load security keys
user=os.getenv('id')
pas=os.getenv('pas')
#load the model
MODEL="CognitiveComputations/dolphin-llama3.1"
#give system prompt
system_message="You are a helpful AI Assistant. If you find any question asking about who you are like ' What's your name? ' , say 'My name is Man.Ai and my creator is Sir Ai-man and I develop by the team called Ai-ManS'"
#crate function for chatinterface 
def chat(message, history):
    messages=[{"role":"system","content":system_message}] + history + [{"role":"user","content":message}]

    stream=ollama.chat(
        model=MODEL,
        messages=messages,
        stream=True
    )
    response = ""
    for chunk in stream:
        response += chunk["message"]["content"] if "message" in chunk else ""
        yield response
#secure the link with id and pass with auth function
gr.ChatInterface(fn=chat,type="messages").launch(share=True,pwa=True,auth=(user,pas))
