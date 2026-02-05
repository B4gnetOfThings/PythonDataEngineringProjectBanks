# Code for ETL operations on Country-GDP data

# Importing the required libraries
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import sqlite3
from datetime import datetime 

url = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
table_attribs = ["Name", "MC_USD_Billion"] #Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion
db_name = 'Banks.db'
table_name = 'Largest_banks'
csv_path = './exchange_rate.csv'
output_path = "./Largest_banks_data.csv"
log_file = "./code_log.txt"

# Suppress generated warnings
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

#Task 1:Logging Function
def log_progress(message):
    timestamp_format = '%Y-%h-%d-%H:%M:%S' # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() # get current timestamp 
    timestamp = now.strftime(timestamp_format) 
    with open("./code_log.txt","a") as f: 
        f.write(timestamp + ' : ' + message + '\n')

# Task 2: Extraction of data
def extract(url, table_attribs):
    page = requests.get(url).text
    soup = BeautifulSoup(page, 'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = soup.find_all("tbody")
    rows = tables[0].find_all("tr")

    for row in rows:
        col = row.find_all("td")
        if len(col) != 0:
            data_dict = {"Name": col[1].find_all("a")[1]["title"],
                         "MC_USD_Billion": float(col[2].contents[0][:-1])}
            df1 = pd.DataFrame(data_dict, index=[0])
            df = pd.concat([df, df1], ignore_index=True)

    return df

# Task 3: Transformation of data
def transform(df, csv_path):

    '''Read the exchange rate CSV file and convert the contents to a
    dictionary so that the contents of the first columns are the keys 
    to the dictionary and the contents of the second column are the
    corresponding values.'''

    exchange_rate = pd.read_csv(csv_path)
    exchange_rate = exchange_rate.set_index('Currency').to_dict()['Rate']

    '''Add MC_GBP_Billion, MC_EUR_Billion, and MC_INR_Billion
    columns to dataframe. Round off to two decimals'''
    df["MC_GBP_Billion"] = [np.round(x * exchange_rate["GBP"], 2) for x in df["MC_USD_Billion"]]
    df["MC_EUR_Billion"] = [np.round(x * exchange_rate["EUR"], 2) for x in df["MC_USD_Billion"]]
    df["MC_INR_Billion"] = [np.round(x * exchange_rate["INR"], 2) for x in df["MC_USD_Billion"]]

    return df

# Task 4: Loading to CSV
def load_to_csv(df, output_path):
    df.to_csv(output_path)

# Task 5: Loading to Database
def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    query_output = pd.read_sql(query_statement, sql_connection)
    print(query_output)



#Call functions and entities

log_progress('Preliminaries complete. Initiating ETL process')

df = extract(url, table_attribs)

log_progress('Data extraction complete. Initiating Transformation process')


df = transform(df, csv_path)

log_progress('Data transformation complete. Initiating loading process')

load_to_csv(df, csv_path)

log_progress('Data saved to CSV file')
print(df)

sql_connection = sqlite3.connect('Banks.db')

log_progress('SQL Connection initiated.')

load_to_db(df, sql_connection, table_name)

log_progress('Data loaded to Database as table. Running the query')

# Call run_query()
# 1. Print the contents of the entire table
query_statement = f"SELECT * from {table_name}"
run_query(query_statement, sql_connection)

# 2. Print the average market capitalization of all the banks in Billion GBP
query_statement = f"SELECT AVG(MC_GBP_Billion) FROM {table_name}"
run_query(query_statement, sql_connection)

# 3. Print only the names of the top 5 banks
query_statement = f"SELECT Name from {table_name} LIMIT 5"
run_query(query_statement, sql_connection)

log_progress("Process Complete")

# Close SQLite3 connection
sql_connection.close()

log_progress("Server Connection closed")

# Task 7: Verify log entries
with open(log_file, "r") as log:
    LogContent = log.read()
    print(LogContent)

