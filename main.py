import load_data
import visualize

if __name__ == '__main__':
    load_data.create_table()
    load_data.load_data('sales_data.csv')
    data = visualize.fetch_data()
    visualize.visualizer(data)