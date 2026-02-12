from flask import Flask, render_template
import qrcode

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=4000, debug=True)
