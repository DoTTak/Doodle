from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    msg = "Hello Flask"
    return render_template("index.html", msg=msg)


app.run(debug=True, port=8888)