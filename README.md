# Chatbot with Gradio and Ollama

## Overview
This project implements a chatbot interface using Gradio and Ollama. The chatbot uses an AI model specified in environment variables and provides responses based on user input and chat history. The interface is secured with authentication credentials loaded from environment variables.

## Features
- **Gradio Chat Interface**: Provides an interactive chat UI.
- **Ollama Integration**: Uses an AI model for response generation.
- **Streaming Responses**: Outputs responses in real-time.
- **Environment Variable Configuration**: Secures sensitive data (model, system prompt, authentication credentials).
- **Authentication**: Requires a user ID and password to access.
- **Progressive Web App (PWA) Support**: Allows installation as a web app.

## Installation
### Prerequisites
- Python 3.8+
- `pip` package manager
- `.env` file with necessary environment variables

### Steps
1. **Clone the Repository**
   ```sh
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Install Dependencies**
   ```sh
   pip install -r requirements.txt
   ```
3. **Set Up Environment Variables**
   Create a `.env` file and add the following:
   ```ini
   id=your_username
   pas=your_password
   model=your_model_name
   system=your_system_prompt
   ```
4. **Run the Chatbot**
   ```sh
   python app.py
   ```

## Usage
1. Open the provided Gradio link.
2. Log in using the credentials set in `.env`.
3. Start chatting with the AI!

## Workflow Diagram
Below is the workflow of the chatbot:
![gradio chatbot workflow diagram](https://github.com/user-attachments/assets/10fd45d1-94f0-4188-96fc-0286e2cf325c)


## File Structure
```
├── app.py                # Main application script
├── .env                  # Environment variables (not included in repo)
├── requirements.txt      # Required dependencies
├── README.md             # Project documentation
```

## Dependencies
- `gradio`
- `ollama`
- `python-dotenv`

Install them with:
```sh
pip install gradio ollama python-dotenv
```

## Security Considerations
- Do not share `.env` files containing credentials.
- Use strong passwords for authentication.
- Consider deploying behind a secure HTTPS server.

## License
This project is licensed under the MIT License.

## Contributing
Feel free to open issues and submit pull requests!

