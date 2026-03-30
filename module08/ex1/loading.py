# import pandas
# import numpy
# import requests
# import matplotlib
import importlib
from types import ModuleType

"""
| Library    | Used for                 |
| ---------- | ------------------------ |
| NumPy      | Math, arrays, matrices   |
| pandas     | Tables, CSV, Excel, data |
| matplotlib | Graphs, plots            |
| requests   | Internet, APIs           |


    Pro tip (real-world workflow)
After installing everything and it works:
$ pip freeze > requirements.txt
This saves the exact working environment.

"""


def compare(modules: list[ModuleType]) -> None:
    """
    comparison function that shows installed package versions
    """
    print("Checking dependencies:")
    source = {
        "pandas": "Data manipulation ready",
        "numpy": "Math, arrays, matrices processor is ready",
        "requests": "Network access ready",
        "matplotlib": "Visualization ready"
    }
    for module in modules:
        name = module.__name__
        version = module.__version__
        print("[OK]", name, f"({version}) - {source[name]}")


def main() -> None:
    missing = []
    imports = ["pandas", "numpy", "requests", "matplotlib"]
    modules = []
    print("\nLOADING STATUS: Loading programs...\n")
    for module in imports:
        try:
            modules.append(importlib.import_module(module))
        except ModuleNotFoundError:
            missing.append(module)
    if len(missing) == 0:
        compare(modules)
        from pandas import DataFrame as df
        from pandas import to_datetime
        import requests as rq
        import numpy as np
        import matplotlib.pyplot as plt
        print("\nAnalyzing Matrix data...")

        # getting data via API
        url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
        params = {
            "vs_currency": "usd",
            "days": "30"}
        response = rq.get(url, params=params)
        data = response.json()
        # here data has to much, i need only prices
        # lets convert into pandas DataFrame
        print(f"Processing {len(data['prices'])} data points...")
        data_frame = df(data["prices"], columns=["Timestamp", "Prices"])
        data_frame["Date"] = to_datetime(data_frame["Timestamp"], unit="ms")
        data_frame["Day"] = data_frame["Date"].dt.date
        avg = np.mean(data_frame["Prices"])
        min = np.min(data_frame["Prices"])
        max = np.max(data_frame["Prices"])
        # plot it
        print("Generating visualization...\n")
        plt.figure()
        plt.plot(data_frame["Date"], data_frame["Prices"])
        plt.title("Bitcoin Price Last 30 Days")
        plt.xlabel("Day")
        plt.ylabel("Price in USD")
        output_filename = "_matrix.png"
        plt.savefig(output_filename)
        plt.show()
        print("Avarage price: ", round(avg, 2),
              "Min price: ", round(min, 2),
              "Max price", round(max, 2))
        print("Analysis complete!")
        print(f"Results saved to: {output_filename}")
    else:
        print("Missing modules: ", missing)
        print("\nto install missing dependencies with pip")
        print("> pip install-r requirements.txt\n",
              "$ python3 loading.py\n",
              "# Should run analysis and create visualization")
        print("\nto install missing dependencies with Poetry:")
        print("poetry install\n",
              "$ poetry run python loading.py\n",
              "# Should run analysis with Poetry environment")


if __name__ == "__main__":
    main()
