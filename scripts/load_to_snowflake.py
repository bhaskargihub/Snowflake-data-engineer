import snowflake.connector
import os

def load_to_snowflake(user, password, account, database='MY_DB', schema='PUBLIC', warehouse='COMPUTE_WH', role=None):
    conn = snowflake.connector.connect(
        user=user,
        password=password,
        account=account,
        warehouse=warehouse,
        database=database,
        schema=schema,
        role=role
    )
    cur = conn.cursor()
    try:
        cur.execute("USE WAREHOUSE {};".format(warehouse))
        cur.execute("USE DATABASE {};".format(database))
        cur.execute("USE SCHEMA {};".format(schema))
        cur.execute("""
        COPY INTO sales_data
        FROM @MY_STAGE/sales_data.csv
        FILE_FORMAT = (TYPE = 'CSV' SKIP_HEADER = 1)
        ON_ERROR = 'CONTINUE';
        """)
        print("✅ Data loaded into Snowflake successfully")
    finally:
        cur.close()
        conn.close()

if __name__ == '__main__':
    # Fill these values before running
    load_to_snowflake(user='YOUR_USER', password='YOUR_PASSWORD', account='YOUR_ACCOUNT')
