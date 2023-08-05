
from flask import Flask, render_template, request
import chatbot

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    response = chatbot.generate_response(user_input)
    return response

if __name__ == '__main__':
    app.run()
