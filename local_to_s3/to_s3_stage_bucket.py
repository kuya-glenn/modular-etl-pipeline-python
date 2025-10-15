import boto3
from botocore.exceptions import ClientError
import os

def upload_to_s3(filename, bucketname, objectName = None):

    if objectName is None:
        objectName = filename

    s3_client = boto3.client('s3')

    try:
        response = s3_client.upload_file(filename, bucketname, objectName)
    
    except ClientError as e:
        print(e)
        return False
    
    return True


filename = ".\\parsed_output\\sample_carmaker_oracle.csv"
bucketname = "aws-bucket-practice1-emv"
objectname = f"landing_local_parsed_vehicle_data/{os.path.basename(filename)}"

upload_to_s3(filename, bucketname, objectname)