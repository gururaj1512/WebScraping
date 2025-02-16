from scrapping import run, importer
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/scrape/<scraper>")
def scrape(scraper):
    return run.run_scrpaer(scraper, request.args.getlist('args'))

@app.route("/import/<scraper_name>", methods=['POST'])
def import_scraper(scraper_name):
    file = request.files['scraper_contents']

    scraper_contents = file.read().decode('utf-8')
    importer.add_scraper(scraper_name, scraper_contents)
    return f"imported {scraper_name}"

def start():
    app.run()
 