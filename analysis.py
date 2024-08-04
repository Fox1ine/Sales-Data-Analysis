import pandas as pd
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import Error
import credentials as cr


def get_connection():
    try:
        connection = psycopg2.connect(
            host=cr.DB_HOST,
            database=cr.DB_NAME,
            user=cr.DB_USER,
            password=cr.DB_PASSWORD
        )
        print("Connection to the database was successful")
        connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        return connection
    except(Exception, Error) as err:
        print("Error while connecting to PostgreSQL", err)
        return None


def analyze_data():
    connection = get_connection()
    if connection is None:
        return None

    try:
        cursor = connection.cursor()
        query = 'SELECT * FROM sales'
        cursor.execute(query)
        rows = cursor.fetchall()

        data = pd.DataFrame(rows, columns=['id', 'date', 'product', 'quantity', 'price'])
        data['month'] = pd.to_datetime(data['date']).dt.to_period('M')
        monthly_sales = data.groupby('month').agg({'quantity': 'sum', 'price': 'sum'}).reset_index()

        return monthly_sales

    except (Exception, Error) as err:
        print("Error while connecting to PostgreSQL", err)

    finally:
        if connection:
            cursor.close()
            connection.close()
            print("PostgreSQL connection is closed")


if __name__ == '__main__':
    monthly_sales = analyze_data()
    if monthly_sales is not None:
        print(monthly_sales.head())
