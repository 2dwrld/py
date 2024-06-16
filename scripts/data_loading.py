# scripts/data_loading.py

import pandas as pd

def load_data(file_path):
    columns = ["symboling", "normalized-losses", "make", "fuel-type", "aspiration",
               "num-of-doors", "body-style", "drive-wheels", "engine-location",
               "wheel-base", "length", "width", "height", "curb-weight", "engine-type",
               "num-of-cylinders", "engine-size", "fuel-system", "bore", "stroke",
               "compression-ratio", "horsepower", "peak-rpm", "city-mpg", "highway-mpg",
               "price"]
    df = pd.read_csv(file_path, names=columns)
    return df