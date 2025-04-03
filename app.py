#import all the libs
import gradio as gr
import ollama
import os
from dotenv import load_dotenv

# load security keys
user=os.getenv('id')
pas=os.getenv('pas')

#load the model
MODEL=os.getenv('model')
#give system prompt
system_message=os.getenv('system')
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
