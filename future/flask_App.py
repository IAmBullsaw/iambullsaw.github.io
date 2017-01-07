from flask import Flask, render_template
from card import Card
from data import Data
import jinja2
app = Flask(__name__)
d = Data()
@app.route('/')
def index():
    d.load_JSON('data.json')
    cards = d.get_cards()
    return render_template('index.html', cards = cards)

if __name__ == '__main__':
    app.run()
