from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "index"

@app.route("/about")
def about():
    return "<h1>МИША БЛЯ</h1>"




if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)