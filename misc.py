import yfinance as yahoo
import matplotlib
from matplotlib import pyplot as plt
from os import path

matplotlib.use("Agg")

plt.style.use("ggplot")


def get_price(symbol: str, period="1d"):
    data = yahoo.Ticker(symbol)
    return data.history(period=period)["Close"].values[0]


def plot_historical_data(symbol: str = "BTC-USD") -> None:
    data = yahoo.Ticker(symbol).history(period="30d")
    plot = data.plot(y="Close", label=symbol)
    fig = plot.get_figure()
    fig.savefig(path.join("static", "images", "plot.png"))


if __name__ == "__main__":
    print(get_price("BTC-USD"))
    plot_historical_data()
