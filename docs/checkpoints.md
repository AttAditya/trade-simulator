# `[DOCS]` Change Checkpoints

The simulator uses checkpoints to determine when to capture snapshots of the trading session. By default, the checkpoints are set to capture snapshots at regular intervals throughout the simulation. However, you can customize these checkpoints to better suit your analysis needs.

## Checkpoint Requirements

- Checkpoints should be a list of `float` with values between `0` and `1`, representing the percentage of completion of the simulation at which snapshots should be taken.
- The checkpoints should be in ascending order, and the last checkpoint should ideally be `1.0` to capture the final state of the simulation.

## Steps to Change Checkpoints

1. **Open the Configuration File**: Navigate to the `src/config.py` file in the project directory.
2. **Change the Checkpoints Variable**: Find the `CHECKPOINTS` variable and update it with your desired list of checkpoints.
3. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now capture snapshots at the new checkpoints you specified.

> TIP: For equally spaced checkpoints, you can use the `CHECKPOINT_COUNT` variable to specify how many checkpoints you want, and the code will automatically generate the appropriate checkpoints for you. Note, that there will be `CHECKPOINT_COUNT` + 1 checkpoints in total, the 1.0 checkpoint is not included in the count.

