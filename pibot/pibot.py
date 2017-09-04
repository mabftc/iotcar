from flask import Flask, render_template, flash, request, session, url_for
from flask_socketio import SocketIO, emit
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'as2dfas1d2ifo3s2sadisfssa23'
socketio = SocketIO(app)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/mobile')
def mobile():
	return render_template('mobile.html')

@socketio.on('update_request')
def handle_message(data):
	print(str(data[u'data'][u'l']))
	emit('telemetry', {"gyro": {"x": random.randrange(1, 5), "y": 9, "z": 0}, "acc": {"x": 1, "y": 2, "z": 3}})

if __name__ == '__main__':
	socketio.run(app, host = '0.0.0.0', debug = False)
