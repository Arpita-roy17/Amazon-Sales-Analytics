import kagglehub
import pandas as pd
import os
import shutil
from pathlib import Path
dataset_id = "thedevastator/unlock-profits-with-e-commerce-sales-data"

download_path = kagglehub.dataset_download(dataset_id)

print("Dataset downloaded successfully!")
print("Downloaded location:", download_path)


csv_files = list(Path(download_path).rglob("*.csv"))

print("\nCSV files found:")
for file in csv_files:
    print(file.name)


raw_folder = Path("data/raw")
raw_folder.mkdir(parents=True, exist_ok=True)


for source_file in csv_files:
    destination = raw_folder / source_file.name
    shutil.copy2(source_file, destination)
    print("Copied:", destination)


if csv_files:
    local_file = raw_folder / csv_files[0].name

    try:
        df = pd.read_csv(local_file, encoding="utf-8")
    except UnicodeDecodeError:
        df = pd.read_csv(local_file, encoding="ISO-8859-1")

    print("\nFirst five rows:")
    print(df.head())

    print("\nDataset information:")
    df.info()

    print("\nDataset shape:")
    print(df.shape)

    print("\nColumn names:")
    print(df.columns.tolist())

else:
    print("No CSV files found!")

print(df.isnull().sum())


print("Duplicate rows:", df.duplicated().sum())


print(df.head())