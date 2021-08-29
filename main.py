from flask import Flask, jsonify, make_response
from flask.globals import request
from send_emails import send_multiple_emails

app = Flask(__name__)


@app.route('/')
def index():
    return jsonify(name="API_SEND_EMAILS", version="0.0.1")


@app.route('/send-emails', methods=["POST", "GET"])
def send_emails():
    email_info = request.get_json()

    if request.method != "POST":
        return make_response(jsonify(type="error", message="user POST method.", status=400),400)

    try:
        message = send_multiple_emails(email_info["emails"], email_info["content"], email_info["subject"])
        return make_response(jsonify(message), message["status"])
    except Exception as e:
        print(e, 'error args')
        return make_response(jsonify(type="error", message="error in body request.", status=422), 422)


if __name__ == '__main__':
    app.run(host="0.0.0.0")

