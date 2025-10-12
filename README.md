Initial Commit - <br/>
  Mapping Generator : Generates JSON file for the data type mapping.<br/>
  Parser : Parse the Data with the mapping generatod. <br/>

Roadmap: <br/>
  Mapping Generator - (Done) <br/>
  Parser - (Done) <br/>
  Load to Staging Database (Oracle/Postgres) - Under Development <br/>
  Transform from staging database - > Load into GCP - Under Development <br/>
  Create a workflow to Automate the process - Data Gathering Stage <br/>
  Create Report from Prod Data - Under Development <br/>

Mapping Generator: <br/>
<img width="727" height="242" alt="image" src="https://github.com/user-attachments/assets/d4ebd3ab-b95c-4b9c-9716-3993440d765b" />
<br/>
  - Creates Mapping in preparation for parsing the data and loading it to Staging Table. <br/>

Data Parser: <br/>
<img width="583" height="350" alt="image" src="https://github.com/user-attachments/assets/d3ce3422-d529-45b4-a9d9-6e71a678d2bd" />
<br/>
Sample Parsed Output: <br/>
<img width="318" height="58" alt="image" src="https://github.com/user-attachments/assets/9302c8f8-8d0d-4ec2-8cf9-d667e0f813f6" />
<br/>
  - Parses the data according to the mapping.json created from Mapping Generator. <br/>
  - Added partitioning support. <br/>
  - Creates a parsed output that will be used to be loaded in the table. <br/>
