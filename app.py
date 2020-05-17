from flask import Flask, render_template
import glob

# glob.glob("/home/adam/*.txt") # file listing, unix-style

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')