from flask import Flask
from flask import render_template

f = Flask(__name__)

@f.route('/')
def index():
    
    return render_template('hello.html')

f.run(debug = True)