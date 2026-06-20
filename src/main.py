from data import SessionData

from pandas import read_csv, DataFrame

from simulator import Simulator

from snapshot import snapshot

from trader_list import trader_agents

from config import (
  CHECKPOINTS,
  DATASET_PATH,
  SNAPSHOT_COLUMNS,
  SNAPSHOT_PATH,
)

data = read_csv(DATASET_PATH)
snapshots = DataFrame(columns=SNAPSHOT_COLUMNS)
sim = Simulator(trader_agents)
total = len(data)
completion = 0

for row in data.itertuples():
  completion += 1
  sim.run_market_day(SessionData(
    row.d, row.o, row.h,
    row.l, row.c, row.v,
  ))

  if completion / total >= CHECKPOINTS[0]:
    CHECKPOINTS.pop(0)
    snapshot(
      trader_agents,
      completion,
      total,
      snapshots,
    )

snapshots.to_csv(SNAPSHOT_PATH, index=False)

