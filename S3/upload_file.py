#!/usr/bin/env python3

import boto3
import botocore

# Upload File to Bucket

client = boto3.client('s3')

try:
    response = client.upload_file('/tmp/test2.txt','pokhriyalbucket','test2.txt')
    print(f"'test2.txt' uploaded successfully")
except botocore.exceptions.ClientError as error:
    print(error)
