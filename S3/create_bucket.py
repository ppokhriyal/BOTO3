#!/usr/bin/env python3

import boto3
import botocore

# Create new Bucket
# Make it Public
# Enable Versioning

client = boto3.client('s3')

try:

    response = client.create_bucket(
            ACL='public-read',
            Bucket='pokhriyalbucket',
            CreateBucketConfiguration={
                'LocationConstraint':'us-east-2'})

    print(f"'pokhriyalbucket' created successfully")
except botocore.exceptions.ClientError as error:
    print(error)

