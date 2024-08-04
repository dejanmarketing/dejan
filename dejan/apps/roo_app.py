# apps/roo_app.py

import click
from dejan.roo import get_roo
from datetime import datetime, timedelta
import pandas as pd

def run_roo_app(date_or_days):
    """
    Handles the main logic for fetching ROO data based on the user's input.
    
    :param date_or_days: A string that is either a specific date (YYYY-MM-DD) or the number of days (7, 30, etc.)
    """
    try:
        # Try to parse as a date first
        try:
            specific_date = datetime.strptime(date_or_days, '%Y-%m-%d').date()
            data = get_roo_data_for_date(specific_date)
        except ValueError:
            # If not a date, treat it as a number of days
            days = int(date_or_days)
            data = get_roo_data_for_days(days)
        
        if isinstance(data, pd.DataFrame):
            print(data.to_string(index=False))
        else:
            print(f"Error: {data}")
    except Exception as e:
        print(f"Error fetching ROO data: {e}")

def get_roo_data_for_date(specific_date):
    """
    Fetches the ROO data for a specific date.

    :param specific_date: The specific date for which to fetch data.
    :return: A DataFrame with the ROO data.
    """
    data = get_roo(2, as_dataframe=True)  # Change '2' to the appropriate search engine
    data['rooDate'] = pd.to_datetime(data['rooDate']).dt.date
    filtered_data = data[data['rooDate'] == specific_date]
    return filtered_data

def get_roo_data_for_days(days):
    """
    Fetches the ROO data for the last 'n' days.

    :param days: The number of days to look back.
    :return: A DataFrame with the ROO data.
    """
    end_date = datetime.now().date()
    start_date = end_date - timedelta(days=days)
    
    data = get_roo(2, as_dataframe=True)  # Change '2' to the appropriate search engine
    data['rooDate'] = pd.to_datetime(data['rooDate']).dt.date
    filtered_data = data[(data['rooDate'] >= start_date) & (data['rooDate'] <= end_date)]
    return filtered_data
