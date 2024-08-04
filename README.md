# Sales-Data-Analysis

## Overview

This project connects to a PostgreSQL database, retrieves sales data, and performs analysis using Python and pandas. The script processes the data to calculate monthly sales totals and quantities. Additionally, the project includes visualization of the analyzed data using matplotlib.

## Features

- **Database Connection:** Securely connects to a PostgreSQL database using credentials stored in environment variables.
- **Data Loading:** Loads sales data from a CSV file into the PostgreSQL database.
- **Data Analysis:** Analyzes the sales data to calculate monthly sales totals and quantities.
- **Data Visualization:** Visualizes the monthly sales data using matplotlib.

## Project Structure

- `analysis.py`: Contains functions to connect to the database and perform data analysis.
- `credentials.py`: Handles the secure retrieval of database credentials from environment variables.
- `load_data.py`: Loads sales data from a CSV file into the database.
- `main.py`: The main script that integrates data loading, analysis, and visualization.
- `sales_data.csv`: A sample CSV file containing realistic and varied sales data.
- `visualize.py`: Contains functions to visualize the analyzed sales data.
