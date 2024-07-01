import os
import json
import boto3
from logs import logger



def get_config():
    configuration_version = os.getenv('CONFIG_VERSION')
    session = boto3.Session(
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY'),
        aws_secret_access_key=os.getenv('AWS_SECRET_KEY')
    )
    s3 = session.client('s3')
    bucket_name = 'weatherapp-configuration'
    file_key = f'configuration/{configuration_version}/configuration.json'
    obj = s3.get_object(Bucket=bucket_name, Key=file_key)
    file_content = obj['Body'].read().decode('utf-8')
    config = json.loads(file_content)
    
    
    if os.getenv('ENVIRONMENT') == 'production':
        return config['prod']
    elif os.getenv('ENVIRONMENT') == 'testing':
        return config['testing']
    else:
        return config['dev']