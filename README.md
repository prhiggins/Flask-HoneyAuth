Flask-HoneyAuth
==============

A modified version of [Flask-HTTPAuth](https://github.com/miguelgrinberg/Flask-HTTPAuth) that adds support for  separately authenticating honey tokens and applying separate code to routes visited by clients using those honey tokens.

Installation
------------
The easiest way to install this is through pip.
```
pip install Flask-HoneyAuth
```

Build Instructions
------------
To build and test the package using docker, first clone the repository:
```
git clone https://github.com/prhiggins/Flask-HoneyAuth.git
```
Then simply build and run the image using the provided Dockerfile:
```
docker build . -t flask-honeyauth && docker run flask-honeyauth
```

Basic authentication example
----------------------------

```python
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
        "dave": generate_password_hash("hey"),
        "alice": generate_password_hash("asdfghj"),
}

def honeyroute():
	return "Hello, %s, welcome to the honey universe!" % auth.current_user()

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

@app.route('/')
@auth.login_required(honey=honeyroute)
def index():
    return "Hello, %s!" % auth.current_user()

if __name__ == '__main__':
    app.run()
```

Note: See the [Flask-HTTPAuth documentation](http://pythonhosted.org/Flask-HTTPAuth) for more complex examples that involve password hashing, custom verification callbacks, and digest and token authentication.

See the [honeybank](http://github.com/prhiggins/honeybank) for more detailed honeypot usage examples.

Author
----------------------------
Patrick Higgins (phiggin5@uoregon.edu)
