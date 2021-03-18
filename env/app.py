from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    #return 'Welcome to my page developed by flask'
    return render_template ('index.html')
@app.route("/hi/")
def code():
    return 'WHO IS THIS?'

@app.route("/hi/<name>")
def say(name):
    return f'Hi there, {name}!'

 
