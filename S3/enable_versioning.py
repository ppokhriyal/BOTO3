#!/usr/bin/env python3

import boto3
import botocore

# Enable Versioning

client = boto3.client('s3')

try:
    response = client.put_bucket_versioning(
            Bucket='pokhriyalbucket',
            VersioningConfiguration={
                'Status':'Enabled'})
    print(f"Versioning enabled on bucket 'pokhriyalbucket'")

except botocore.exceptions.ClientError as error:
    print(error)
