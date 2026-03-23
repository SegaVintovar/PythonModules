# import pandas
# import numpy
# import requests
# import matplotlib
import importlib
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

missing = []
imports = ["pandas", "numpy", "requests", "matplotlib"]
for module in imports:
    try:
        importlib.import_module(module)
    except ModuleNotFoundError:
        missing.append(module)
if len(missing) == 0:
    from pandas import DataFrame as df
    import requests
    print("do some stuff")
    # getting data via API
    url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
    params = {
        "vs_currency": "usd",
        "days": "30"}
    response = requests.get(url, params=params)
    data = response.json()
    # lets convert into pandas DataFrame
    print(type(response), response)
    print(type(data), data)
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