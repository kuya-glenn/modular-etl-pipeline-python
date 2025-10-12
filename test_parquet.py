import pandas as pd

landing_dir = r"C:\Users\Juan\Desktop\ING\parsed_output"
filename = "sample_carmaker_oracle.csv.paquet"
df = pd.read_parquet(f"{landing_dir}\\{filename}")
print(df.dtypes)