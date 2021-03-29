#!/usr/bin/env python3

import boto3
import botocore

# Delete Bucket Object

client = boto3.client('s3')

try:
    #list all bucket versions
    object_dict={}
    response = client.list_object_versions(
            Bucket='pokhriyalbucket')
    for i in response['Versions']:
        object_dict['Key'] = i['Key']
        object_dict['VersionId'] = i['VersionId']
        response2 = client.delete_objects(
                Bucket='pokhriyalbucket',
                Delete={
                    'Objects': [object_dict]})

except botocore.exceptions.ClientError as error:
    print(error)
