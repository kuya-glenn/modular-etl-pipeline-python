import oracledb
import pandas as pd
import sys
## To be encrypted
connStr = "system/root@localhost:1521/xe"


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

def insert_query(df, tbl_name):
    cols = df.columns.to_list()
    col_toStr = ', '.join(cols)
    placeholder = ', '.join([f':{i+1}' for i in range(len(cols))])
    return f"INSERT INTO {tbl_name} ({col_toStr}) VALUES ({placeholder})"

def insert_oracle(df, tbl_name, batch_size):
    rows = [tuple(row) for row in df.to_numpy()]
    query = insert_query(df, tbl_name)

    with oracledb.connect(connStr) as conn:
        with conn.cursor() as cur:
            print("Connection established")
            total_insert = 0

            try:
                for i in range(0, len(rows), batch_size):
                    batch = rows[i:i + batch_size]
                    cur.executemany(query, batch)
                    conn.commit()
                    total_insert += len(batch)
                print(f"Total inserted {total_insert}")
            
            except Exception as e:
                conn.rollback()
                raise e

    print(f"Inserted {total_insert} rows into {tbl_name}.")

def main(parsed_output, tbl_name, batch_size):
    try:
        df = load_PARSED_OUTPUT(parsed_output)


        print("Connection established")

        print(f"Inserting data to {tbl_name}")
        insert_oracle(df, tbl_name, batch_size)

    except Exception as e:
        print('Error while connecting to oracle db')
        print(e)

    finally:
        print("Execution Completed")

if __name__ == "__main__":
    parsed_output = sys.argv[1]
    tbl_name = sys.argv[2]
    batch_size = sys.argv[2]
    main(parsed_output, tbl_name, batch_size)