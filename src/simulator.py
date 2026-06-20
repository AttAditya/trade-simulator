from data import SessionData

from traders.base import Trader

class Simulator:
  def __init__(self, traders_list: list[Trader]):
    self.last: SessionData | None = None
    self.data = {f for f in "dohlcv"}
    self.traders = traders_list

  def run_market_day(self, data: SessionData):
    if self.last is None:
      self.last = data
      return

    for trader in self.traders:
      bid, qty = trader.suggest_bid(self.last)
      trader.last_session = data
      balance = trader.balance

      if data.low_price <= bid <= data.high_price:
        balance.cash -= bid * qty
        balance.asset += qty

        if qty < 0:
          balance.credits += 1

        if qty > 0:
          balance.debits += 1

    self.last = data

