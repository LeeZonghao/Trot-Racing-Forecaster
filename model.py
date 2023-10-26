import pandas as pd
import numpy as np
import torch
import os

dataset_name = "trots_2013-2022.parquet"

# Define the root directory where you want to start the search
root_directory = 'D:/data'  # Start from the root of your file system

# Function to search for a dataset by name
def find_dataset(root_dir, dataset_name):
    for root, dirs, files in os.walk(root_dir):
        if dataset_name in files or dataset_name in dirs:
            return os.path.join(root, dataset_name)
    return None

# Search for the dataset
dataset_path = find_dataset(root_directory, dataset_name)
df=pd.read_parquet(dataset_path, engine='pyarrow')

# read the dataset
df.shape
df.head()
df.info()