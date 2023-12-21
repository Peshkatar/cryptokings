# type: ignore
import numpy as np
from typing import TypeAlias
from misc import get_price

volume: TypeAlias = float
price: TypeAlias = float


class Portfolio:
    def __init__(self, assets=dict[str, tuple[volume, price]]) -> None:
        self._assets = assets
        self._paid = np.array([price for _, price in assets.values()])
        self._volume = np.array([volume for volume, _ in assets.values()])
        self._symbols = list(self._assets.keys())

    def get_return(self, pct: bool = False) -> np.array:
        current_prices = np.array([get_price(symbol) for symbol in self._symbols])
        returns = (current_prices - self._paid) * self._volume
        return returns if not pct else returns / (self._paid * self._volume)


def main() -> None:
    ASSETS = {
        "ADA-USD": (10, 0.3),
        "ETH-USD": (1, 1884),
    }
    portfolio = Portfolio(ASSETS)
    print(f"ADA: {get_price('ADA-USD'):.3f} ETH {get_price('ETH-USD'):.3f}")
    print(
        f"{np.array2string(portfolio.get_return(), formatter={'float': lambda x: f'{x:.3f}'})}"
    )
    print(
        f"{np.array2string(portfolio.get_return(pct=True), formatter={'float': lambda x: f'{x:.3%}'})}"
    )
    portfolio.plot_historical_data()


if __name__ == "__main__":
    main()
