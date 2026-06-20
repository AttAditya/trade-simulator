from traders.base import Trader

class MomentumMonkeyV2(Trader):
  def __init__(
    self,
    capacity: int = 10,
    momentum: int = 5,
  ):
    super().__init__("Momentum Monkey V2")
    self.momentum = momentum
    self.capacity = capacity
    self.prices = []
    self.up = 0
    self.dn = 0
    self.quantity = 100
    self.collected = 0

  def suggest_bid(self, prev_data):
    self.prices.append(prev_data.close_price)

    if len(self.prices) > self.capacity:
      val = self.prices.pop(0)

      if val < self.prices[0]:
        self.up -= 1
      else:
        self.dn -= 1

    if len(self.prices) >= 2:
      if self.prices[-2] < self.prices[-1]:
        self.up += 1
      else:
        self.dn += 1

    if self.up >= self.momentum:
      self.collected += self.quantity

      return prev_data.close_price, self.quantity

    if self.dn >= self.momentum:
      sell_qty = min(self.quantity, self.collected)
      self.collected -= sell_qty

      return prev_data.close_price, -sell_qty

    return prev_data.close_price, 0

