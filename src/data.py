class SessionData:
  def __init__(
    self,
    timestamp: int,
    open_price: float,
    high_price: float,
    low_price: float,
    close_price: float,
    volume: float
  ):
    self.timestamp = timestamp
    self.open_price = open_price
    self.high_price = high_price
    self.low_price = low_price
    self.close_price = close_price
    self.volume = volume

class WealthBalance:
  def __init__(
    self,
    cash_balance: float = 0.0,
    asset_balance: float = 0.0,
  ):
    self.cash = cash_balance
    self.asset = asset_balance
    self.credits = 0
    self.debits = 0

  def total_wealth(self, current_price: float) -> float:
    return self.cash + (self.asset * current_price)

