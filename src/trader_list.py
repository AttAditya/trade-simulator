from traders.feel import FeelTrader
from traders.long import LongTermTrader
from traders.momentum_v1 import MomentumMonkeyV1
from traders.momentum_v2 import MomentumMonkeyV2
from traders.momentum_v3 import MomentumMonkeyV3
from traders.trench import TrenchTrader

alternate_trench = [
  TrenchTrader(0.02),
  TrenchTrader(0.03),
  TrenchTrader(0.05),
  TrenchTrader(0.07),
  TrenchTrader(0.1),
]

alternate_monkeys_v1 = [
  MomentumMonkeyV1(3),
  MomentumMonkeyV1(10),
  MomentumMonkeyV1(15),
  MomentumMonkeyV1(20),
  MomentumMonkeyV1(25),
]

alternate_monkeys_v2 = [
  MomentumMonkeyV2(10, 3),
  MomentumMonkeyV2(10, 5),
  MomentumMonkeyV2(10, 6),
  MomentumMonkeyV2(10, 7),
  MomentumMonkeyV2(10, 8),
]

alternate_monkeys_v3 = [
  MomentumMonkeyV3(10, 2, 4),
  MomentumMonkeyV3(10, 3, 4),
  MomentumMonkeyV3(10, 5, 4),
  MomentumMonkeyV3(10, 5, 2),
  MomentumMonkeyV3(10, 5, 3),
]

best_traders = [
  LongTermTrader(),
  FeelTrader(),
  TrenchTrader(0.01),
  MomentumMonkeyV1(7),
  MomentumMonkeyV2(10, 2),
  MomentumMonkeyV3(10, 2, 3),
]

for idx, monkey in enumerate(alternate_trench):
  monkey.name = f"[Alternate] Trench Trader {idx + 1}"

for idx, monkey in enumerate(alternate_monkeys_v1):
  monkey.name = f"[Alternate] Momentum Monkey V1 {idx + 1}"

for idx, monkey in enumerate(alternate_monkeys_v2):
  monkey.name = f"[Alternate] Momentum Monkey V2 {idx + 1}"

for idx, monkey in enumerate(alternate_monkeys_v3):
  monkey.name = f"[Alternate] Momentum Monkey V3 {idx + 1}"

trader_agents = [
  *alternate_trench,
  *alternate_monkeys_v1,
  *alternate_monkeys_v2,
  *alternate_monkeys_v3,
  *best_traders,
]

