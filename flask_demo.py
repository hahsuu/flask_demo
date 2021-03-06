from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return "Index"


@app.route('/hello')
def hello():
    return "Hello World!"


@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' %username


if __name__ == '__main__':
    app.debug = True
    app.run()
