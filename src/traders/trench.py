from traders.base import Trader

class TrenchTrader(Trader):
  def __init__(self, depth: float = 0.05):
    super().__init__("Trench Trader")
    self.depth = depth

  def suggest_bid(self, prev_data):
    return prev_data.close_price * (1 - self.depth), 100

