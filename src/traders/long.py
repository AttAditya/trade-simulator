from traders.base import Trader

class LongTermTrader(Trader):
  def __init__(self):
    super().__init__("Long Term Trader")
    self.bought = False

  def suggest_bid(self, prev_data):
    if not self.bought:
      self.bought = True

      return prev_data.close_price, 100

    return prev_data.close_price, 0

