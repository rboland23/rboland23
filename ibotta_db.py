# Importing relevant models
import sqlite3
import pandas as pd
import os

### sqlite3: This module is used to interact with SQLite databases.
### pandas: This library is used for data manipulation and analysis, particularly for reading CSV files into DataFrames.
### os: This module provides functions to interact with the operating system, particularly for checking if files exist.

class CSVtoSQLiteLoader:
    def __init__(self, db_name):
        #Initialize the DatabaseLoader with the database name.
        self.db_name = db_name
        self.conn = None
        self.connect_db()
  
    def connect_db(self):
        #Connect to the SQLite database.
        self.conn = sqlite3.connect(self.db_name)
        print(f"Connected to database {self.db_name}")

    def load_csv_to_db(self, csv_file_path, table_name):
        ## Load data from a CSV file into the specified table in the database
        df = pd.read_csv(csv_file_path)
        df.to_sql(table_name, self.conn, if_exists='replace', index=False)
        print(f"Closed connection to database {self.db_name}")

    def close_db(self):
        # Close the database connection.
        self.conn.close()
        print(f"Closed connection to database {self.db_name}")

###__init__ Method: This is the constructor method. It initializes the CSVtoSQLiteLoader object with the database name and establishes a connection to the database by calling the connect_db method.
### connect_db Method: This method connects to the SQLite database specified by db_name and prints a confirmation message.
### load_csv_to_db Method: This method reads a CSV file into a pandas DataFrame and then writes the DataFrame to the specified table in the SQLite database. If the table already exists, it replaces the table. It also prints a message confirming the data load.
### close_db Method: This method closes the database connection and prints a confirmation message.


def main():
    # Main function to load CSV files into the SQLite database.
    db_name = '/Users/ryanboland/Downloads/ibotta.db'
    csv_files = {
        # List of CSV files and table names
        'customer_offer_rewards': '/Users/ryanboland/Downloads/customer_offer_rewards_144392.csv',
        'customer_offers': '/Users/ryanboland/Downloads/customer_offers_296332.csv',
        'offer_rewards': '/Users/ryanboland/Downloads/offer_rewards_168083.csv',
        'customer_offer_redemptions': '/Users/ryanboland/Downloads/customer_offer_redemptions_31025.csv'
    }

    loader = CSVtoSQLiteLoader(db_name)

    for table_name, csv_file in csv_files.items():
        if os.path.exists(csv_file):
            loader.load_csv_to_db(csv_file, table_name)
        else:
            print(f"File {csv_file} does not exist.")

    loader.close_db()

### main Function: This function manages the entire process of loading CSV files into the SQLite database.
### Database Name: Specifies the path to the SQLite database (ibotta.db).
### CSV Files Dictionary: Contains the mappings between table names and the corresponding CSV file paths.
### CSVtoSQLiteLoader Instance: Creates an instance of the CSVtoSQLiteLoader class.
### Loading Data: Iterates over the CSV files. For each file, it checks if the file exists using os.path.exists. If the file exists, it calls load_csv_to_db to load the data into the corresponding table. If the file does not exist, it prints an error message.
### Closing the Database: Calls close_db to close the database connection.

    
# Run the main function
if __name__ == "__main__":
    main()
### This block checks if the script is being run as the main module and calls the main function to start the data-loading process.  

### Summary: 
### The script is designed to load data from multiple CSV files into a SQLite database.
### It uses object-oriented programming (OOP) principles for better organization and reusability.
### The script ensures that the database connection is properly managed and provides feedback on the operations performed.
