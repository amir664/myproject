import flask
from flask import Flask

app = Flask(__name__)

@app.route("/")

def home():
    return "Hello, Flask! Your application is mnot running brother hahahahhah."



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
