# `[DOCS]` Changing Output CSV File

The simulator saves a CSV file with snapshots of the simulation at given checkpoints. The CSV file is saved in the `output/` directory of the project.

## Steps to change the Output CSV File

1. **Update the Configuration**: Go to the `src/config.py` file and update the `SNAPSHOT_PATH` variable to point to your new dataset file.
2. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now save the output CSV file in the new location you specified in the `SNAPSHOT_PATH` variable.

## Change the internal Saving Metrics

1. **Update the column names**: Navigate to the `src/config.py` file in the project directory. Change the `SNAPSHOT_COLUMNS` variable to include the new column names you want to save in the output CSV file. Make sure to keep the order of the columns consistent with the data being saved.
2. **Update the snapshot saving logic**: Navigate to the `src/snapshot.py` file in the project directory. Update the `store_trader(Trader, float, pandas.DataFrame) -> None` function to reflect the new column names.
3. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now save the output CSV file with the new column names you specified in the `SNAPSHOT_COLUMNS` variable and the updated saving logic in the `store_trader` function.

> Note: Although the simulator is designed to be flexible and can work with different datasets, it is important to ensure that the new column names and saving logic are consistent with the data being saved. Otherwise, the output CSV file may not be generated correctly. Snapshot module was designed for a specific use case, modifying is easy but caution is advised.

