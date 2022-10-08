from flask import Flask, render_template

app = Flask(__name__)

@app.route("/primeiro")
def primeiro():
    return render_template("primeiro.html")

@app.route("/index")
def index():
    return render_template("index.html")


@app.route("/ajuda")
def ajuda():
    return render_template("ajuda.html")


if __name__ == "__main__":
    app.run(debug=True)