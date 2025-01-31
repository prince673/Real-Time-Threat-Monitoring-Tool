from flask import Flask , render_template
from flask_socketio import SocketIO
import threading
import time 

app = Flask(__name__)
Socketio = SocketIO(app)

threats = []

@app.route('/')
def index ():
    return render_template('index.html')

@Socketio.on('connect')
def handle_connect():
    Socketio.email('update_threat', threats)

def log_threat_to_dashboard(message):
    threats = {'message': message , 'timestamp': time.strftime("%Y-%m-%d %H:%M:%S")}
    threats.append(threats)
    Socketio.emit("new_threat found", threats)

def start_dashboard():
    print("[*] Starting Dashboard on http://localhost:5000")
    Socketio.run(app,host='0.0.0.0',port=5000)