from flask import Flask, render_template, request
from misc import plot_historical_data

app = Flask(__name__)


@app.route("/")
def index():
    plot_historical_data()
    return render_template(
        "index.html", name="Close price", url="static/images/plot.png"
    )


# TODO: kolla om det går att stoppa in detta i index()
@app.route("/plot", methods=["GET", "POST"])  # type: ignore
def plot():
    if request.method == "GET":
        return "The URL /plot is accessed directly. Try going to '/' to submit form"

    # kanske onödig if-sats
    if request.method == "POST":
        form_data = request.form
        plot_historical_data(form_data["symbol"])
        return render_template(
            "index.html", name="Close price", url="static/images/plot.png"
        )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True, port=8000)
