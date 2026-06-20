# `[DOCS]` Change Logs

The logs are not part of the core functionality of the simulator, they are happening via a separate module which is capturing data inside all the active elements.

The logs were designed for a specific use case, although they can be easily modified to capture different data or to be stored in a different format.

## Steps to Change Logs

1. **Open the Snapshot Module**: Navigate to the `src/snapshot.py` file in the project directory.
2. **Change the Log Function**: Change the `log` function to capture the data you want.
3. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now capture logs according to the new specifications you set in the `log` function.

