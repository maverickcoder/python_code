import pandas as pd
import snowflake.connector
from configparser import ConfigParser
config=ConfigParser()

config.read(r'C:\Users\kujjwal\.ipynb_checkpoints\config.ini')
user=config['database']['user']
password=config['database']['password']
account=config['database']['account']
warehouse=config['database']['warehouse']
database=config['database']['database']
schema=config['database']['schema']
 

 
 
conn = snowflake.connector.connect(
            user=user,
            password=password,
            account=account,
            warehouse=warehouse,
            database=database,
            schema=schema
            )

cur = conn.cursor()

# Execute a statement that will generate a result set.
sql = "select * from ES2_DAILY_USAGE ;"
cur.execute(sql)
# Fetch the result set from the cursor and deliver it as the Pandas DataFrame.
df = cur.fetch_pandas_all()
 
path='mediye'
df.to_csv(r'C:\Users\kujjwal\Documents\MyStuff\MyProjects\SnowflakeDataExtractor\{}.csv'.format(path),
          encoding='utf-8', index=False, sep='|')