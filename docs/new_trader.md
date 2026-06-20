# `[DOCS]` New Trader

The traders are the core of the simulator, they are the ones who are making the decisions and executing the trades. The traders are designed to be easily modifiable, so you can create your own trading strategies and test them in the simulator.

## Steps to Optimize an Existing Trader

In case of optimizing a parameter of an existing trader instead of creating a new one, you can follow the same steps but instead of creating a new class, you can modify the existing one.

1. **Open the Trader List Module**: Navigate to the `src/trader_list.py` file in the project directory.
2. **Change or create a new trader**: Call a trader class with the desired parameters and add it to the `trader_agents` list variable.
3. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now use your new trader.

## Steps to Create a New Trader

1. **Create a New Trader Class**: Create a new class inside the `src/traders/` directory that inherits from the `Trader` base class (`class YourTrader(Trader):`). Make sure to implement the required methods - `suggest_bid(Self, SessionData) -> tuple[float, int]`.
2. **Follow the Optimization Steps**: Follow the steps above to add your new trader to the `trader_agents` list variable in the `src/trader_list.py` file.
3. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now use your new trader.

