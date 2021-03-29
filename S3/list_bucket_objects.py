#!/usr/bin/env python3

import boto3
import botocore

# List Objects from Bucket

client = boto3.client('s3')

try:
    response = client.list_objects_v2(
            Bucket='pokhriyalbucket')
    if len(response['Contents']) == 0:
        print("Bucket is empty")
    else:
        for i in response['Contents']:
            print(i['Key'])

except botocore.exceptions.ClientError as error:
    print(error)
