from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from flask_socketio import SocketIO
from routs.host_routes import hosst_routes_blueprint

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})
socketio = SocketIO(app, cors_allowed_origins="http://localhost:3000")

app.register_blueprint(hosst_routes_blueprint)

@app.route('/')
def index():
    data ={'data': 'This text was fetched using an HTTP call to server on render'}
    return jsonify(data)


@socketio.on('connect')
def handle_host_event(data):
    # Handle your socket connection logic here
    #print(f"Received host event: {data}")
    socketio.emit('host_response', {'data': 'Response from server connect'})

@socketio.on('from react')
def handle_test_event(data):
    # Handle your logic for the 'test' event here
    print(f"Received test event with data: {data}")
    # You can also emit a response back to the client if needed
    socketio.emit('test_response', {'data': 'Response from server test'})

if __name__ == '__main__':
    socketio.run(app, debug=True, use_reloader=False, allow_unsafe_werkzeug=True)

