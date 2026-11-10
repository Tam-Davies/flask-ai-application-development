
from flask import Flask, render_template, request

my_app = Flask(__name__)

@my_app.route('/')
def home():
    return "Welcome to my Flask application!"

@my_app.route('/sample/')
def get_sample_html():
    return render_template('sample.html')

@my_app.route('/user/<username>', methods=['GET', 'POST'])
def greet_user(username):
    return render_template('result.html', username=username)

@my_app.route('/user', methods=['GET'])
def greet_user_based_on_req():
    user_name = request.args.get('username')
    return render_template('result.html', username=user_name)

if __name__ == "__main__":
    my_app.run(debug=True)
