-- Example of promoting raw data into analytics table (simple example)
CREATE OR REPLACE TABLE sales_data AS
SELECT id, date, amount FROM sales_data_raw;
