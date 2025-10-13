import data_parser as parser

## Add parsing stage for a datasource
## Sample Run: "landing dir", "filename", "parsed output directory", "parser mapping configuration directory", "parser_mapping"
parser.main(r".\landing_dir", "sample_carmaker_oracle.csv", r".\parsed_output", r".\parser_mapping", "vehicleData_mapping.json")