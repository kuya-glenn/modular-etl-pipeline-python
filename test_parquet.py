import pandas as pd

landing_dir = r".\parsed_output"
filename = "sample_carmaker_oracle.csv.paquet"
df = pd.read_parquet(f"{landing_dir}\\{filename}")
print(df.applymap(lambda x: isinstance(x, pd._libs.missing.NAType)).sum())
print(len(df))
#print(df.columns.to_list())
#columns = df.columns.tolist()
#col_str = ', '.join(columns)
#placeholders = ', '.join([f':{i+1}' for i in range(len(columns))])

#print(columns)
#print(col_str)
#print(placeholders)
#tupy = [tuple(row) for row in df.to_numpy()]
#print(tupy[0])