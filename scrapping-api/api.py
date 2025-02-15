from scrapping import run, output
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/scrape/<scraper>")
def scrape(scraper):
    return run.run_scrpaer(scraper, request.args.getlist('args'))

def start():
    app.run()
 