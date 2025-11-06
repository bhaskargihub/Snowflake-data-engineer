-- Create an external stage pointing to the S3 bucket (replace MY_STAGE and bucket URL)
CREATE OR REPLACE STAGE MY_STAGE
URL = 's3://my-snowflake-bucket/input/'
STORAGE_INTEGRATION = my_s3_integration
FILE_FORMAT = my_csv_format;
