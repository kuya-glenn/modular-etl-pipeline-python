# API Extraction - Transformation - Loading <br/>

## Objective
  Demonstrate ability to create a pipeline from scratch using **Python**, **OracleDB**, **Google BigQuery** or **AWS S3**

## Completed
  **Mapping Generator** : Generates JSON file for the data type mapping. <br/>
  **Parser** : Parse the Data with the mapping generated. Added Data Model Verification <br/>
  **Data Loader** : Loads data to OracleDB staging Table. <br/>

## **Roadmap** <br/>
  ### Fetch Data from API - **(Done)** <br/>
  ### Fetch Data from S3 Bucket - _Under Development_ <br/>
  ### Mapping Generator - **(Done)** <br/>
  ### Parser - **(Done)** <br/>
  ### Load to Staging Database (Oracle/Postgres) - **(Done)** <br/>
  ### Transform from staging database - > Load into GCP - _Under Development_ <br/>
  ### Create a workflow to Automate the process - _Data Gathering Stage_ <br/>
  ### Create Report from Prod Data - _Under Development_ <br/>

## Mapping Generator <br/>
<img width="727" height="242" alt="image" src="https://github.com/user-attachments/assets/d4ebd3ab-b95c-4b9c-9716-3993440d765b" />
<br/>
  - Creates Mapping in preparation for parsing the data and loading it to Staging Table. <br/>

## Data Parser <br/>
<img width="583" height="350" alt="image" src="https://github.com/user-attachments/assets/d3ce3422-d529-45b4-a9d9-6e71a678d2bd" /> <br/>

## Sample Parsed Output <br/>
<img width="318" height="58" alt="image" src="https://github.com/user-attachments/assets/9302c8f8-8d0d-4ec2-8cf9-d667e0f813f6" />
<br/>
  - Parses the data according to the mapping.json created from Mapping Generator. <br/>
  - Added partitioning support. <br/>
  - Creates a parsed output that will be used to be loaded in the table. <br/>

 ## Data Loader Flow: <br/>
  Get Data from Parsed Output - > Load Data to Dataframe - > Remove NaN values - > Batch insert data to Staging Table. <br/>

  ### Sample Data Loader run <br/>
  <img width="411" height="130" alt="image" src="https://github.com/user-attachments/assets/4931ac8c-5c38-430f-8ecf-f29f291f4340" /> <br/>

  ### Loaded to Sample Table <br/>
  <img width="1783" height="374" alt="image" src="https://github.com/user-attachments/assets/ebcb83d0-b249-4a26-b62e-a0d91ddc9f84" /> <br/>

## Future Plans <br/>
  - Mapping Generator : <br/>
      - Add target table for Dataload script to use <br/>
  - Parsing : <br/>
      - Add manual config for parsing_stg and mapping.json destination files. This will: <br/>
        - Make the script re-runnable for multiple data source/feed <br/>
        - Can be automated for multiple data source/feed <br/>
  - Data Loader : <br/>
      - Use mapping.json for parsed_output destination definition. This will: <br/>
        - Users will no longer define the variables inside the script. <br/>
        - Can make the script re-runnable with multiple data source/feed <br/>
  - Create Data Workflow via Nifi. In this case it will simulate: <br/>
      - Informatica Workflow <br/>
      - Talend Workflow <br/>
      - Cloud Platforms (GCP/AWS) <br/>
  - Add Kafka to decouple data extraction, transformation, and loading stages: <br/>
      - Use Kafka Topics to stream Data between ETL components. <br/>
      - Improve Scalability and fault tolerance. <br/>
      - Enable near real-time processing and modular architecture. <br/>
