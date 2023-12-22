from flask import Flask, render_template, request
from misc import plot_historical_data

app = Flask(__name__)


@app.route("/")
def index():
    plot_historical_data()
    return render_template(
        "index.html", name="Close price", url="static/images/plot.png"
    )


@app.route("/plot", methods=["GET", "POST"])  # type: ignore
def plot():
    if request.method == "GET":
        return "The URL /data is accessed directly. Try going to '/form' to submit form"

    if request.method == "POST":
        form_data = request.form
        plot_historical_data(form_data["symbol"])
        return render_template(
            "index.html", name="Close price", url="static/images/plot.png"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
