from flask import Flask
app = Flask(__name__)

@app.route('/')
def greet():
    return 'Hello, World!'

@app.route('/greet')
def greet_me():
    return 'Hi therr'


if __name__ == '__main__':
    app.run(debug=True)
