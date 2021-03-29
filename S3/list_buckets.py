#!/usr/bin/env python3

# List all Buckets

import boto3
import botocore

client = boto3.client('s3')

response = client.list_buckets()

if len(response['Buckets']) == 0:
    print("Buckets not found")
else:
    for each_bucket in response['Buckets']:
        print(each_bucket)
