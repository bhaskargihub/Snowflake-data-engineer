-- COPY from stage into raw table
COPY INTO sales_data_raw (id, date, amount)
FROM @MY_STAGE/sales_data.csv
FILE_FORMAT = (FORMAT_NAME = my_csv_format)
ON_ERROR = 'CONTINUE';
