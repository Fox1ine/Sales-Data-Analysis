import pandas as pd
import psycopg2
from psycopg2 import Error
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import analysis


def fetch_data():
    return analysis.analyze_data()


def visualizer(data):

    if data is None or data.empty:
        print("No data to visualize")
        return None

    monthly_sales = data

    fig, ax1 = plt.subplots()

    ax2 = ax1.twinx()
    ax1.bar(monthly_sales['month'].astype(str), monthly_sales['quantity'], color='g')
    ax2.plot(monthly_sales['month'].astype(str), monthly_sales['price'], color='r')

    ax1.set_xlabel('Month')
    ax1.set_ylabel('Quantity', color='b')
    ax2.set_ylabel('Price', color='r')

    plt.title('Monthly Sales Data')
    plt.show()


if __name__ == '__main__':
    data = fetch_data()
    visualizer(data)
