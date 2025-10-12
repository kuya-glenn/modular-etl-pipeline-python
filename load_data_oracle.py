import pandas as pd
import oracledb

# Initialize Oracle client
oracledb.init_oracle_client(
    lib_dir=r"C:\Oracle\instantclient-basic-windows.x64-23.9.0.25.07\instantclient_23_9"
)

# Connection details
username = "system"
password = "root"
dsn = "localhost:1521/xe"

# Read parquet file and replace NaN with None
df = pd.read_parquet("sample_carmaker_oracle.parquet")
df = df.astype(object).where(pd.notnull(df), None)

# Connect to Oracle
conn = oracledb.connect(user=username, password=password, dsn=dsn)
cursor = conn.cursor()

# Build insert query dynamically
columns = df.columns.tolist()
col_str = ", ".join(columns)
bind_str = ", ".join([f":{i+1}" for i in range(len(columns))])
sql = f"INSERT INTO vehicle_data_staging ({col_str}) VALUES ({bind_str})"

# Convert DataFrame to list of rows
data = df.values.tolist()

# Insert in batches
batch_size = 500  # adjust batch size based on dataset size
for i in range(0, len(data), batch_size):
    batch = data[i:i+batch_size]
    cursor.executemany(sql, batch)
    conn.commit()  # commit per batch to avoid huge transactions

# Close connections
cursor.close()
conn.close()

print(f"Inserted {len(data)} rows into vehicle_data_staging successfully.")
