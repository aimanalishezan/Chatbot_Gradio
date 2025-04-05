# import all the libs
import gradio as gr
import ollama
import os
from dotenv import load_dotenv

# load .env keys
load_dotenv()
user = os.getenv('id')
pas = os.getenv('pas')
MODEL = os.getenv('model')
system_message = os.getenv('system')

# define chatbot function
def chat(message, history):
    messages = [{"role": "system", "content": system_message}] + history + [{"role": "user", "content": message}]
    stream = ollama.chat(model=MODEL, messages=messages, stream=True)
    response = ""
    for chunk in stream:
        response += chunk["message"]["content"] if "message" in chunk else ""
        yield response

# custom CSS
custom_css = """
#header {
    text-align: center;
    padding: 20px;
    background: linear-gradient(to right, #111827, #1f2937);
    color: #f3f4f6;
    font-family: 'Segoe UI', sans-serif;
    border-radius: 12px;
    margin-bottom: 20px;
}

#header h1 {
    font-size: 2.5rem;
    margin: 0;
    font-weight: bold;
    color: #38bdf8;
}

#header h3 {
    font-weight: normal;
    font-size: 1rem;
    margin-top: 8px;
    color: #9ca3af;
}
"""

# interface layout
with gr.Blocks(css=custom_css) as demo:
    with gr.Column():
        with gr.Row():
            gr.HTML("""
            <div id="header">
                <h1>🤖 MAN_Ai</h1>
                <h3>Developed by Ai_MAN</h3>
            </div>
            """)
        gr.ChatInterface(fn=chat, type="messages")

# launch app with auth
demo.launch(share=True, pwa=True, auth=(user, pas))
