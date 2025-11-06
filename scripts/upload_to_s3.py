import boto3
import os

def upload_to_s3(local_file='data/sales_data.csv', bucket='my-snowflake-bucket', s3_path='input/sales_data.csv'):
    s3 = boto3.client('s3')
    if not os.path.exists(local_file):
        raise FileNotFoundError(f"Local file not found: {local_file}")
    s3.upload_file(local_file, bucket, s3_path)
    print(f"✅ File uploaded to s3://{bucket}/{s3_path}")

if __name__ == '__main__':
    upload_to_s3()
