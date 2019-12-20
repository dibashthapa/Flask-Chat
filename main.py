from flask import *
from flask_socketio import SocketIO, send, emit
app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")
app.secret_key = "dibashthapa"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/submit',methods=['POST','GET'])
def submit():
    if (request.method=='POST'):
        Name=request.form['Name']
        session['Name']=Name
        return redirect('/chat')
    else:
        return redirect('/')

@app.route('/chat',methods=['POST','GET'])
def run_chat():
    if 'Name' in session:
        Name=session['Name']
        return render_template("chats.html",Name=Name)
    else:
        return redirect('/')
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
    socketio.run(app,debug=True)
