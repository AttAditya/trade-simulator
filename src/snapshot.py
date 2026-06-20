def log(traders):
  print()
  print(
    "======================="
    "======================="
    "======================="
  )

  highest = traders[0]
  lowest = traders[0]
  highest_total = float("-inf")
  lowest_total = float("inf")

  for trader in traders:
    balance = trader.balance
    total = balance.asset
    total *= trader.last_session.close_price
    total += balance.cash

    if total >= highest_total:
      highest = trader
      highest_total = total

    if total <= lowest_total:
      lowest = trader
      lowest_total = total

    print(trader)
    print()

  print()
  print()
  print("Highest:", highest)
  print()
  print("Lowest:", lowest)
  print()
  print()

def store_trader(trader, completion, results):
  balance = trader.balance
  current_price = trader.last_session.close_price
  total_wealth = balance.total_wealth(current_price)
  results.loc[len(results.index)] = {
    "completion": float(f"{completion:.4f}"),
    "trader_name": trader.name,
    "cash": balance.cash,
    "asset_count": balance.asset,
    "asset_cash": balance.asset * current_price,
    "credit_count": balance.credits,
    "debit_count": balance.debits,
    "total_wealth": total_wealth
  }

def store(traders, completion, results):
  for trader in traders:
    store_trader(trader, completion, results)

def snapshot(traders, completion, total, results):
  print(f"Progress: {completion}/{total}")
  store(traders, completion / total, results)
  log(traders)

