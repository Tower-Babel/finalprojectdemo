from flask import Flask, render_template
from flask_socketio import SocketIO




## socetIO is a cross-browser js lib
## enable encryption by declaring a SECKET_KEY

app = Flask(__name__)
app.config['SECRET_KEY'] = 'redrumredrum123#'
socketio = SocketIO(app)



@app.route('/')
def sessions():
    return render_template('session.html')

def messageReceieved(methods=["PUT, GET, POST, DELETE, OPTIONS"]):
    print('message was recieved sucessfully!')

@socketio.on('my event')
def handle_my_custom_event(json, methods=["PUT, GET, POST, DELETE, OPTIONS"]):
    print('recieved my event: ' +str(json))
    socketio.emit('my response', json, callback=messageReceieved)

if __name__ == '__main__':
    socketio.run(app, debug=True)