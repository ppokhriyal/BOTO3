#!/usr/bin/env python3

import boto3
import botocore

# Delete Bucket

client = boto3.client('s3')

try:
    response = client.delete_bucket(
            Bucket = 'pokhriyalbucket')
    print(response)

except botocore.exceptions.ClientError as error:
    print(error)
