from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "DaDing Bot Running 🚀"

if name == "__main__":
    app.run(host="0.0.0.0", port=10000)
