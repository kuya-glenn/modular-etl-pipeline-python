import data_loading as data_loading

## usage ("input file", "target table", batch size)

## Add Pipelines Here
## vehicle data pipeline
data_loading.main(r".\PARSED_OUTPUT\sample_carmaker_oracle.csv.paquet", "vehicle_data_staging", 5)