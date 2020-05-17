from flask import Flask, render_template
import glob

# glob.glob("/home/adam/*.txt") # file listing, unix-style

app = Flask(__name__)

@app.route('/')
def home():
    tech_list = glob.glob('templates/tech/[!_]*.html')
    tech_list = list(map(lambda s : s.replace('templates/', '', 1), tech_list))
    return render_template('index.html', tech_list=tech_list)
