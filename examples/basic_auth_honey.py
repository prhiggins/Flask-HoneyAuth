#!/usr/bin/env python
"""Basic authentication example, with honey auth check

This example demonstrates how to protect Flask endpoints with basic
authentication, using secure hashed passwords.

After running this example, visit http://localhost:5000 in your browser. To
gain access, you can use (username=john, password=hello) or
(username=susan, password=bye).
"""
from flask import Flask
from flask_honeyauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()

users = {
    "john": generate_password_hash("hello"),
    "susan": generate_password_hash("bye")
}

honey_users = {
    "dave": generate_password_hash("hacked"),
    "alice": generate_password_hash("asdfghj")
}

@auth.verify_password
def verify_password(username, password):
    if username in users and check_password_hash(users.get(username),
                                                 password):
        return username


@auth.check_honeytoken
def check_honeytoken(auth):
	if auth.username in honey_users and check_password_hash(honey_users.get(username), auth.password):
		return auth.username
	else:
		return False

def alternative_route():
	return "Hello, %s, this is a honey route, special for you!" % auth.current_user()

@app.route('/')
@auth.login_required(honey=alternative_route)
def index():
    return "Hello, %s!" % auth.current_user()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
