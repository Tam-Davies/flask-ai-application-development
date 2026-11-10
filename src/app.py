from flask import Flask, render_template, request


my_app = Flask(__name__)

@my_app.route('/')
def hello_world():
    return 'Hello World'

if __name__ == "__main__":
    my_app.run(debug=True)