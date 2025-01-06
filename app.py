from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<p>Hello, World!</p>"

@app.route("/predict")
def home():
    return "predict.hello"


if __name__ == '__main__':
    app.run(debug=True)