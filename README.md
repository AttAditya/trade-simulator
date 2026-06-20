# Trade Simulator

## Introduction

This project goes over a dataset, analyzes it, and then uses it by replaying it in a custom-built trading market simulator to evaluate the performance of different trade agents implementing different trading strategies, and then analyzes the results.

## How to setup the simulator

1. Clone this repository.
2. Create a virtual environment and activate it.
3. Install dependencies using `pip install -r requirements.txt`.
4. Run the main simulation using `python src/main.py`.

## How to change or add to the project

Check out the [`docs/`](./docs) folder for documentation, it contains information and steps to allow modification for specific aspects of the project that can be customized.

## In this repository

| Folder | Description |
| --- | --- |
| [`data`](./data) | Contains the dataset used for the project. |
| [`docs`](./docs) | Contains documentation for the project, including how to add new trader agents and how the simulator works. |
| [`notebook`](./notebook) | Contains Jupyter notebooks for preliminary analysis and results. |
| [`outputs`](./outputs) | Contains output files generated from the simulation runs. (files were moved) |
| [`plots`](./plots) | Contains generated plots from the analysis. |
| [`report`](./report) | Contains the project report and related images. |
| [`src`](./src) | Contains the source code for the project, including the main simulation and trader agent implementations. |


## Project Structure

```tree
.
├── .gitignore
├── LICENSE
├── README.md
├── data
│   └── 1000BONKUSDT.csv
├── docs
│   ├── README.md
│   ├── change_dataset.md
│   ├── checkpoints.md
│   ├── logs.md
│   ├── new_trader.md
│   └── output_csv.md
├── log.txt
├── notebook
│   ├── preliminary_notebook.ipynb
│   └── result_notebook.ipynb
├── outputs
│   ├── log.txt
│   └── snapshots.csv
├── plots
│   ├── preliminary
│   │   ├── global_candle_chart.png
│   │   ├── global_line_chart.png
│   │   ├── high_close_relativity_chart.png
│   │   ├── open_close_relativity_chart.png
│   │   ├── volume_close_relativity_chart.png
│   │   ├── zoomed_candle_chart.png
│   │   └── zoomed_line_chart.png
│   └── result
│       ├── monkey_v2_v3_chart.png
│       ├── traders_total_wealth_chart.png
│       └── traders_total_wealth_normalized_chart.png
├── report
│   ├── README.md
│   ├── Report.pdf
│   └── images
│       ├── global_candle_chart.png
│       ├── global_line_chart.png
│       ├── high_close_relativity_chart.png
│       ├── monkey_v2_v3_chart.png
│       ├── open_close_relativity_chart.png
│       ├── traders_total_wealth_chart.png
│       ├── traders_total_wealth_normalized_chart.png
│       ├── volume_close_relativity_chart.png
│       ├── zoomed_candle_chart.png
│       └── zoomed_line_chart.png
├── requirements.txt
├── snapshots.csv
└── src
    ├── __init__.py
    ├── config.py
    ├── data.py
    ├── main.py
    ├── simulator.py
    ├── snapshot.py
    ├── trader_list.py
    └── traders
        ├── __init__.py
        ├── base.py
        ├── feel.py
        ├── long.py
        ├── momentum_v1.py
        ├── momentum_v2.py
        ├── momentum_v3.py
        └── trench.py
```

## License

[MIT License](./LICENSE)

## Author

[Aditya Prasad Dash](https://github.com/AttAditya)

