from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO, join_room, leave_room, send, emit
import flask_cors
from logutil import logger
import time


app = Flask(__name__)
socketio = SocketIO(app)
log = logger()

@socketio.on('connect')
def test_connect(auth):
    join_room(auth["group"])
    emit('connected', {'data': 'Connected'})

@app.route("/admin")
def admin_interface():
    return render_template('admin.html',participant_id=log.participant_id)

@app.route("/participant")
def participant_interface():
    return render_template('participant.html')

@app.route("/help")
def help():
    log.log()
    emit("help_request", {"data": time.time()}, broadcast=True, namespace="/")
    return ("",200)

@app.route("/p_msg", methods=["POST"])
def p_msg():
    data = request.form
    log.log(data["msg"])
    emit("help_response", {"msg": data["msg"]}, broadcast=True, namespace="/")
    return redirect("/admin")

@app.route("/p_info", methods=["POST"])
def p_info():
    data = request.form
    participant_id = data["pid"]
    log.set_participant_id(participant_id)
    return redirect("/admin")


if __name__ == '__main__':
    socketio.run(app)