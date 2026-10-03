from flask import Flask
import socket

app = Flask(__name__)

@app.get("/")
def home():
    return {
        "message": "DevOps Lab is alive",
        "hostname": socket.gethostname()
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
