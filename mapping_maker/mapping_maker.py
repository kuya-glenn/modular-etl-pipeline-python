import json

def make_mapping():
    mapping = {"columns" : {}}

    print("Enter mapping (type done when finished):")
    while True:
        colName = input("Column Name:")
        if colName.lower() == 'done':
            print(mapping)
            break
        colType = input("Enter Column Datatype (string, int, float, double, datetime): ")
        colInfo = {"type": colType}

        if colType.lower() == "datetime":
            date_format = input("Date Format [US] or [NS]: ")
            colInfo["format"] = date_format.upper()

        mapping["columns"][colName] = colInfo

    partition = input("Partition the data? (y/n): ")
    if partition.lower() == 'y':
        partition_col = input("enter partition column name: ")
        mapping["partition_column"] = partition_col

    fileType = input("File type (parquet is the only available now. Only save in parquet!): ")
    #if fileType.lower() == 'parquet':
    mapping["fileType"] = fileType

    filename = input("Enter mapping filename (mapping_config.json): ")
    landing_dir = r".\parser_mapping"
    with open(f"{landing_dir}\\{filename}", 'w') as f:
        json.dump(mapping, f, indent=4)
    
    print(f"mapping saved to {filename}")

if __name__ == '__main__':
    make_mapping()