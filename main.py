from flask import *
from flask_socketio import SocketIO, send, emit
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.secret_key = "dibashthapa"
@app.route('/')
def index():
    return render_template("index.html")
@app.route('/chat',methods=['POST','GET'])
def run_chat():
    if (request.method=='POST'):
        Name=request.form['Name']
        return render_template("chats.html",Status=True,Name=Name)
    else:
        return render_template("chats.html")
@socketio.on("typing",namespace='/message')
def send_typing(data):
    print(data['names'],"is typing...")
    emit('data typing',data,broadcast=True)
@socketio.on('message from user',namespace='/message')
def handleMessage(data):
    messages=data['messages']
    print(messages)
    emit('from flask',data,broadcast=True)

if __name__ == '__main__':
    socketio.run(app,host='192.168.1.65',debug=True)
