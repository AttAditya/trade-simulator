from random import randint

from traders.base import Trader

class FeelTrader(Trader):
  def __init__(self):
    super().__init__("Feel Trader")

  def suggest_bid(self, prev_data):
    return (
      prev_data.close_price * (
        1 + (randint(-5, 5) / 100)
      ), 100
    )

