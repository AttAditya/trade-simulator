from data import SessionData, WealthBalance

class Trader:
  def __init__(self, name: str):
    self.name = name
    self.balance = WealthBalance()
    self.last_session = SessionData(0, 0, 0, 0, 0, 0)

  def suggest_bid(
    self, prev_data: SessionData
  ) -> tuple[float, int]:
    return 0.0, 0

  def __repr__(self):
    balance = self.balance
    cashed = self.last_session.close_price * balance.asset
    total = balance.cash + cashed
    transactions = balance.credits + balance.debits
    result = f"{self.name}:"
    result += f"\n+---------+"
    result += f"\n| Credits | {balance.credits:.0f}"
    result += f"\n| Debits  | {balance.debits:.0f}"
    result += f"\n| Total   | {transactions:.0f}"
    result += f"\n+---------+"
    result += f"\n| Cash    | {balance.cash:.4f}"
    result += f"\n| Asset   | {balance.asset:.0f}"
    result += f"\n| Cashed  | {cashed:.4f}"
    result += f"\n| Total   | {total:.4f}"
    result += f"\n+---------+"

    return result

