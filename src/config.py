DATASET_PATH = "data/1000BONKUSDT.csv"
SNAPSHOT_PATH = "outputs/snapshots.csv"
CHECKPOINT_COUNT = 100
SNAPSHOT_COLUMNS = [
  "completion", "trader_name",
  "cash", "asset_count", "asset_cash",
  "credit_count", "debit_count", "total_wealth"
]

CHECKPOINTS = [
  i / CHECKPOINT_COUNT for i in range(CHECKPOINT_COUNT)
] + [1.0]

