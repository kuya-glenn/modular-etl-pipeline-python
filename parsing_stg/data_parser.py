import json
import pandas as pd
import pyarrow
import os
import sys

## Will implement filename matching on future updates

def main(landing_dir, filename, parsed_output, mapping_dir, mapping_filename):

    print(f"Loading Mapping File: {mapping_filename}\n")
    with open(f"{mapping_dir}\\{mapping_filename}", 'r') as f:
        mapping = json.load(f)
    #print(mapping)

    print(f"Mapping file loaded: {mapping_filename}\n")

    if os.path.exists(f"{landing_dir}\\{filename}"):
        print(f"Loading data to dataframe: {filename}\n")
        df = pd.read_csv(f"{landing_dir}\\{filename}")
        df.columns = df.columns.str.lower()
    else:
        print(f"No data in the landing dir")
        exit()
    #print(df.columns)

    print("Mapping Datatypes")
    for col, info in mapping["columns"].items():
        #col_type = info["type"]
        #p
        if col in df.columns:
            dataType = info["type"].lower()

            #print(f"{col} -- {info} || {info["type"]}")
            print(f"{col if col else 'N/A'} --> {info["type"]}")
            if dataType == "string":
                df[col] = df[col].astype("string")

            elif dataType == "int":
                df[col] = df[col].astype("int64")

            elif dataType == "float" or dataType == "double":
                df[col] = df[col].astype("float")

            elif dataType == "object":
                df[col] = df[col].astype("object")

            elif dataType == "datetime":
                format = info.get("format", "US").upper()

                if format == "US":
                    df[col] = df[col].astype("datetime64[us]")
                else:
                    df[col] = df[col].astype("datetime64[ns]")
            # df[col] = df[col].astype("object")
            else:
                print(f"Skipping {df[col]} : Unknown type {dataType}")

    #print(df.dtypes)

    partition_col = mapping.get("partition_column")



    partition_col = mapping.get("partition_column")
    file_type = mapping.get("fileType")
    print(f"\nFile type: {file_type}")

    if partition_col and partition_col in df.columns:
        for key, val in df.groupby(partition_col):
            if file_type == "parquet":
                df.to_parquet(f"{parsed_output}\\{partition_col}={key}\\{filename}.paquet", engine="pyarrow", index=False)
                print(f"file successfully parsed to {parsed_output}\\{partition_col}={key}\\{filename}.paquet")
    else:
        df.to_csv(f"{parsed_output}\\{filename}", index=False)
        print(f"File successfully parsed to {filename}")

if __name__ == "__main__":
    landing_dir = sys.argv[1]
    filename = sys.argv[2]
    parsed_output = sys.argv[3]

    ## Sample Filename for ingestion
    mapping_dir = sys.argv[4]
    mapping_filename = sys.argv[5]
    main(landing_dir, filename, parsed_output, mapping_dir, mapping_filename)