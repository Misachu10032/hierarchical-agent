import os
from flask import Flask
from flask_socketio import SocketIO, emit
from supervisor_graph import super_graph
import time
from dotenv import load_dotenv  # Import dotenv
from flask_cors import CORS

# Load API keys from .env file
load_dotenv()

# Access API keys securely
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
LANGSMITH_API_KEY = os.getenv("LANGSMITH_API_KEY")

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Allow Vue frontend to connect
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")  # Allow WebSocket connections


@app.route('/')
def index():
    return "Server is running"  

@socketio.on('connect')
def handle_connect():
    print("Client connected")

@socketio.on('ask_question')
def handle_question(data):
    question = data['question'] 
    print(f"Received question: {question}")

    for s in super_graph.stream({"messages": [("user", question)]}, {"recursion_limit": 150}):
        # Convert object to string (or dict) before emitting
        if isinstance(s, str):  
            response = s  
        else:
            response = str(s)  # Convert to string

        emit('stream_data', response)
        print(response)
        time.sleep(1)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
