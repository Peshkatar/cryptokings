from flask import Flask, render_template
from misc import plot_historical_data

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/plot")  # type: ignore
def plot():
    plot_historical_data()
    return render_template(
        "plot.html", name="Close price", url="static/images/plot.png"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
