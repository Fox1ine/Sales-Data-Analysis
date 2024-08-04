import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
import analysis


def create_table():
    try:
        connection = analysis.get_connection()
        cursor = connection.cursor()

        create_table_query = '''
        CREATE TABLE IF NOT EXISTS sales (
            id SERIAL PRIMARY KEY,
            date DATE NOT NULL,
            product VARCHAR(255) NOT NULL,
            quantity INTEGER NOT NULL,
            price NUMERIC NOT NULL
        );
        '''
        cursor.execute(create_table_query)
        print("Table 'sales' created successfully or already exists.")

        cursor.close()
        connection.close()

    except (Exception, Error) as err:
        print("Error while connecting to PostgreSQL", err)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


def load_data(file_path):
    data = pd.read_csv(file_path)
    try:
        connection = analysis.get_connection()
        if connection is None:
            return

        cursor = connection.cursor()

        for index, row in data.iterrows():
            cursor.execute("""
                INSERT INTO sales (date, product, quantity, price) 
                VALUES (%s, %s, %s, %s)
            """, (row['date'], row['product'], row['quantity'], row['price']))

        cursor.close()
        connection.close()

    except (Exception, Error) as err:
        print("Error while connecting to PostgreSQL", err)
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    create_table()
    load_data('sales_data.csv')
