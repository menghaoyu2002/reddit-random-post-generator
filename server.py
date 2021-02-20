from typing import NoReturn
from randompost import RandomPost
from flask import Flask, render_template, redirect
app = Flask(__name__)
import webbrowser

randompost = RandomPost()

@app.route('/')
def index():
  return render_template('/index.html')

@app.route('/redirect/')
def get_post():
    randompost.get_random_post()
    return render_template('/index.html')

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000/")
    app.run()


