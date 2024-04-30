# -*- coding: utf-8 -*-
"""banks_project.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/11LDxjOsOZKIqgDb5qBCnWlq1hbtHyqb_
"""

import datetime

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    # Get the current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log message
    log_message = f"{current_time} : {message}\n"

    # Write the log message to the file
    with open("code_log.txt", "a") as log_file:
        log_file.write(log_message)

import pandas as pd
from bs4 import BeautifulSoup
import requests

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    log_progress("Started extracting data from the URL.")

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table under the heading 'By market capitalization'
    table = soup.find('span', {'id': 'By_market_capitalization'}).find_next('table')

    # Convert the HTML table to a DataFrame
    df = pd.read_html(str(table))[0]

    log_progress("Data extraction completed successfully.")

    return df

# Test extract function
data_df = extract("https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks", table_attribs={'class': 'wikitable sortable'})
print(data_df)

import pandas as pd
import numpy as np

def transform(data_df):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # Define arbitrary exchange rates for demonstration
    exchange_rates = {'GBP': 0.8, 'EUR': 0.93, 'INR': 82.95}  # Manually typed in the Exchange rates, as am having troubles reading the file using colab.

    # Convert market capitalization to GBP and EUR based on arbitrary exchange rates
    data_df['MC_GBP_Billion'] = data_df['Market cap (US$ billion)'] * exchange_rates['GBP']
    data_df['MC_EUR_Billion'] = data_df['Market cap (US$ billion)'] * exchange_rates['EUR']
    data_df['MC_INR_Billion'] = data_df['Market cap (US$ billion)'] * exchange_rates['INR']

    # Round the values to 2 decimal places
    data_df = data_df.round({'MC_GBP_Billion': 2, 'MC_EUR_Billion': 2, 'MC_INR_Billion': 2})

    log_progress("Data transformation completed successfully.")

    return data_df

# Test transform function
transformed_df = transform(data_df)
print(transformed_df)

def load_to_csv(transformed_df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

    # Save DataFrame to CSV file
    transformed_df.to_csv(output_path, index=False)

    # Log the progress
    log_progress("Data saved to CSV file")

# Define the output path for the CSV file
output_path = "top_10_banks_market_cap.csv"

# Function call for load_to_csv()
load_to_csv(transformed_df, output_path)

import sqlite3

def load_to_db(transformed_df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

    # Establish a connection to the SQLite3 database
    conn = sqlite3.connect(sql_connection)

    # Save DataFrame to SQLite database
    transformed_df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

    # Log the progress
    log_progress("Data loaded to Database as a table. Executing queries")

# Define the SQL connection and table name
sql_connection = "Banks.db"
table_name = "Largest_banks"

# Function call for load_to_db()
load_to_db(transformed_df, sql_connection, table_name)

def run_queries(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    # Establish a connection to the SQLite3 database
    conn = sqlite3.connect(sql_connection)

    # Execute the query
    cursor = conn.cursor()
    cursor.execute(query_statement)

    # Fetch and print the query output
    query_output = cursor.fetchall()
    print("Query Statement:", query_statement)
    print("Query Output:")
    for row in query_output:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Log the progress
    log_progress("Process Complete")

# Define the query statements
query1 = "SELECT * FROM Largest_banks"
query2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
query3 = "SELECT Name FROM Largest_banks LIMIT 5"

# Function calls for run_queries()
run_queries(query1, sql_connection)
run_queries(query2, sql_connection)
run_queries(query3, sql_connection)

import os

# Remove the existing code_log.txt file
if os.path.exists("code_log.txt"):
    os.remove("code_log.txt")
    print("Existing code_log.txt file removed successfully.")

# Execute the final run of the code

import datetime

def log_progress(message):
    ''' This function logs the mentioned message of a given stage of the
    code execution to a log file. Function returns nothing'''

    # Get the current timestamp
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Format the log message
    log_message = f"{current_time} : {message}\n"

    # Write the log message to the file
    with open("code_log.txt", "a") as log_file:
        log_file.write(log_message)

import pandas as pd
from bs4 import BeautifulSoup
import requests

def extract(url, table_attribs):
    ''' This function aims to extract the required
    information from the website and save it to a data frame. The
    function returns the data frame for further processing. '''

    log_progress("Started extracting data from the URL.")

    # Send a GET request to the URL
    response = requests.get(url)

    # Parse HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table under the heading 'By market capitalization'
    table = soup.find('span', {'id': 'By_market_capitalization'}).find_next('table')

    # Convert the HTML table to a DataFrame
    df = pd.read_html(str(table))[0]

    log_progress("Data extraction completed successfully.")

    return df

# Test extract function
data_df = extract("https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks", table_attribs={'class': 'wikitable sortable'})
print(data_df)

import pandas as pd
import numpy as np

def transform(data_df):
    ''' This function accesses the CSV file for exchange rate
    information, and adds three columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies'''

    # Define arbitrary exchange rates for demonstration
    exchange_rates = {'GBP': 0.8, 'EUR': 0.93, 'INR': 82.95}  # Manually typed in the Exchange rates, as am having troubles reading the file using colab.

    # Convert market capitalization to GBP and EUR based on arbitrary exchange rates
    data_df['MC_GBP_Billion'] = data_df['Market cap (US$ billion)'] * exchange_rates['GBP']
    data_df['MC_EUR_Billion'] = data_df['Market cap (US$ billion)'] * exchange_rates['EUR']
    data_df['MC_INR_Billion'] = data_df['Market cap (US$ billion)'] * exchange_rates['INR']

    # Round the values to 2 decimal places
    data_df = data_df.round({'MC_GBP_Billion': 2, 'MC_EUR_Billion': 2, 'MC_INR_Billion': 2})

    log_progress("Data transformation completed successfully.")

    return data_df

# Test transform function
transformed_df = transform(data_df)
print(transformed_df)

def load_to_csv(transformed_df, output_path):
    ''' This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing.'''

    # Save DataFrame to CSV file
    transformed_df.to_csv(output_path, index=False)

    # Log the progress
    log_progress("Data saved to CSV file")

# Define the output path for the CSV file
output_path = "top_10_banks_market_cap.csv"

# Function call for load_to_csv()
load_to_csv(transformed_df, output_path)


import sqlite3

def load_to_db(transformed_df, sql_connection, table_name):
    ''' This function saves the final data frame to a database
    table with the provided name. Function returns nothing.'''

    # Establish a connection to the SQLite3 database
    conn = sqlite3.connect(sql_connection)

    # Save DataFrame to SQLite database
    transformed_df.to_sql(table_name, conn, if_exists='replace', index=False)

    # Close the connection
    conn.close()

    # Log the progress
    log_progress("Data loaded to Database as a table. Executing queries")

# Define the SQL connection and table name
sql_connection = "Banks.db"
table_name = "Largest_banks"

# Function call for load_to_db()
load_to_db(transformed_df, sql_connection, table_name)


def run_queries(query_statement, sql_connection):
    ''' This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. '''

    # Establish a connection to the SQLite3 database
    conn = sqlite3.connect(sql_connection)

    # Execute the query
    cursor = conn.cursor()
    cursor.execute(query_statement)

    # Fetch and print the query output
    query_output = cursor.fetchall()
    print("Query Statement:", query_statement)
    print("Query Output:")
    for row in query_output:
        print(row)

    # Close the cursor and connection
    cursor.close()
    conn.close()

    # Log the progress
    log_progress("Process Complete")

# Define the query statements
query1 = "SELECT * FROM Largest_banks"
query2 = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
query3 = "SELECT Name FROM Largest_banks LIMIT 5"

# Function calls for run_queries()
run_queries(query1, sql_connection)
run_queries(query2, sql_connection)
run_queries(query3, sql_connection)




# Print the result
print("Final execution completed.")

# Open and print the contents of code_log.txt file
try:
    with open("code_log.txt", "r") as log_file:
        print("\nLog Entries:")
        for line in log_file:
            print(line.strip())
except FileNotFoundError:
    print("code_log.txt file not found.")