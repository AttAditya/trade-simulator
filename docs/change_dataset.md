# `[DOCS]` Using a different dataset

The simulator is designed to be flexible and can work with different datasets. As long as the dataset is in the correct format (CSV with specific columns), you can easily switch to a different dataset.

## Dataset Format

The dataset should be a CSV file with the following columns:
- `d`: Timestamp of the data point (in milliseconds since epoch)
- `o`: Open price
- `h`: High price
- `l`: Low price
- `c`: Close price
- `v`: Volume

## Steps to Use a Different Dataset

1. **Prepare Your Dataset**: Ensure your dataset is in the correct format as described above. You can use any historical price data that follows this structure.
2. **Place the Dataset**: Save your dataset CSV file in the `data/` directory of the project.
3. **Update the Configuration**: Go to the `src/config.py` file and update the `DATASET_PATH` variable to point to your new dataset file.
4. **Run the Simulation**: Execute the main simulation script using `python src/main.py`. The simulator will now use your new dataset for the analysis and trading simulation.

