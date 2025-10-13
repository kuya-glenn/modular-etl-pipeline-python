import oracledb
import pandas as pd

## To be encrypted
connStr = "system/root@localhost:1521/xe"

PARSED_OUTPUT = r"C:\Users\Juan\Desktop\ING\PARSED_OUTPUT\sample_carmaker_oracle.csv.paquet"
TBL_NAME = "vehicle_data_staging"
BATCH_SIZE = 5

def load_PARSED_OUTPUT(path):
    try:
        df = pd.read_parquet(path)
        for col in df.columns:
            df[col] = df[col].apply(lambda x: None if pd.isna(x) else x)
        #df = df.where(pd.notnull(df), None)
        return df
    
    except Exception as e:
        print("Error has occured. Please check data to be loaded")
        raise e

def insert_query(df):
    cols = df.columns.to_list()
    col_toStr = ', '.join(cols)
    placeholder = ', '.join([f':{i+1}' for i in range(len(cols))])
    return f"INSERT INTO {TBL_NAME} ({col_toStr}) VALUES ({placeholder})"

def insert_oracle(df):
    rows = [tuple(row) for row in df.to_numpy()]
    query = insert_query(df)

    with oracledb.connect(connStr) as conn:
        with conn.cursor() as cur:
            print("Connection established")
            total_insert = 0

            try:
                for i in range(0, len(rows), BATCH_SIZE):
                    batch = rows[i:i + BATCH_SIZE]
                    cur.executemany(query, batch)
                    conn.commit()
                    total_insert += len(batch)
                print(f"Total inserted {total_insert}")
            
            except Exception as e:
                conn.rollback()
                raise e

    print(f"Inserted {total_insert} rows into {TBL_NAME}.")

def main():
    try:
        df = load_PARSED_OUTPUT(PARSED_OUTPUT)


        print("Connection established")

        print(f"Inserting data to {TBL_NAME}")
        insert_oracle(df)

    except Exception as e:
        print('Error while connecting to oracle db')
        print(e)

    finally:
        print("Execution Completed")

if __name__ == "__main__":
    main()