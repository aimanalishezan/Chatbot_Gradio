import gradio as gr
import ollama

MODEL="CognitiveComputations/dolphin-llama3.1"

system_message="You are a helpful AI Assistant. If you find any question asking about who you are like ' What's your name? ' , say 'My name is Man.Ai and my creator is Sir Ai-man and I develop by the team called Ai-ManS'"

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

gr.ChatInterface(fn=chat,type="messages").launch(share=True,pwa=True)