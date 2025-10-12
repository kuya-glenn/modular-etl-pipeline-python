import requests
import pandas as pd
import time
import random
from datetime import datetime, timedelta
import pyarrow

url = "https://vpic.nhtsa.dot.gov/api/vehicles/getallmanufacturers"
results_api = []
landing_dir = r".\landing_dir"

## in case of rate limiting, implement back off
maxRetries = 5
## Will fetch data from paginated REST API endpoint

## Create sleep duration
def sleepDuration(Attempt):
    sleep = 2 ** Attempt + random.random()
    return sleep

## Create func for sleep duration
def willSleep(duration):
    print(f"Waiting Duration {duration}")
    time.sleep(duration)

for page in range(1,6):
    print(f"Fetching Page {page}")
    params = {"format":"json", "page": page}

    for attempt in range(1, maxRetries + 1):

        try:
            response = requests.get(url, params=params)

            if response.status_code == 200:              
                data = response.json()
                results = data.get("Results", [])

                results_api.extend(results)
                print(f"Page {page} fetched successfully")
                print(sleepDuration(attempt))
                if not results:
                    print("No more data.")
                    break
                break
            
            else: 
                print(f"Attempt {attempt} failed: ({response.status_code})")
                sleep_duration = sleepDuration(attempt)
                willSleep(sleep_duration)
            
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: Exception error occurred : {e}")
            sleep_duration = sleepDuration(attempt)
            willSleep(sleep_duration)

            

## Load data to dataframe 
df = pd.DataFrame(results_api)
current_date = datetime.now()
df["date_fetched"] = current_date
df["date_fetched"] = pd.to_datetime(df["date_fetched"])

"""
## Add dynamic mapping
dataMapping = {
    "Country" : "string",
    "Mfr_CommonName" : "string",
    "Mfr_ID" : "int64",
    "Mfr_Name" : "string",
    "VehicleTypes" : "string",
    "date_fetched" : "datetime[us]"
}

for col, dtype in dataMapping.items():
    if col in df.columns:
        if "datetime" in dtype:
            df[col] = df[col].astype("datetime64[us]")
        elif dtype == "string":
            df[col] = df[col].astype("string")
        elif dtype == "object":
            df[col] = df[col].astype("object")
        elif dtype == "int64":
            df[col] = df[col].astype("int64")
        else:
            print("skipping mapping, datatype not found")
            continue
"""
print(df.dtypes)
print(df.head())

filename = "sample_carmaker_oracle.csv"
df.to_csv(f"{landing_dir}\\{filename}", index=False)
#df.to_csv("car_makers.csv", index=False)

