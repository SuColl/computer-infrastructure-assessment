#! /usr/bin/env python

# import NumPy to manipulate numerical arrays
import numpy as np
# import Python Data Analysis Library
import pandas as pd
# import Matplotlib.PyPlot for plotting
import matplotlib.pyplot as plt
# import yfinance for financial data for these exercises
# https://github.com/ranaroussi/yfinance
import yfinance as yf
# Library for handling date and time data, https://docs.python.org/3/library/datetime.html
import datetime as dt
# Library for interfacing with the operating system, https://docs.python.org/3/library/os.html
import os 
# Library for regular expressions, used for string matching
import re

# Function to download hourly finance data for specified stock trackers
def get_finance_data_hourly(ticker_list, period='5d'):
    """Download Yahoo Finance data for supplied list of trackers, default period 5 days."""

    # Use the yfinance.download function with multiple stock tickers
    downloaded_dataframe = yf.download(ticker_list, period=period, interval='1h', auto_adjust=True)

    # Look at the first 5 rows of the resulting DataFrame.
    print(f"Downloaded DataFrame Head: \n {downloaded_dataframe.head(5)}")
    return(downloaded_dataframe)


# Function to generate the CSV filename for data output from the current time
def csv_filename_from_now():
    "Generate the CSV data output filename from the current time"
    # Current date and time.
    now = dt.datetime.now()

    # Show.
    print(f"Current date and time are {now}.")

    # Use datetime.datetime.strftime to create the output filename as a string, 
    # in the requested format.  
    # Handy cheat sheet for strftime format specifiers available at
    # https://strftime.org/ 
    csv_filename = now.strftime("%Y%m%d-%H%M%S.csv")
    print(f"Generated CSV filename is {csv_filename}.")

    # Return the 
    return csv_filename


# Function to check if a directory exists
def check_directory(directory_to_check):
    """Check if a specified directory exists, if not, create the directory."""
    if not os.path.isdir(directory_to_check):
        os.makedirs(directory_to_check)
        print(f"Created directory at {directory_to_check}")
    else:
        print(f"Directory exists at {directory_to_check}")


# Function to download all hourly finance data, and export to CSV file
def get_data():
    # Download hourly stock data
    df_downloaded = get_finance_data_hourly(tickers)

    # Check for output data directory
    check_directory(data_output_dir)
    
    # Generate the filename fo the output data
    data_output_filename = csv_filename_from_now()

    # Write DataFrame to CSV file in data directory.
    df_downloaded.to_csv(data_output_dir + data_output_filename)
    print(f"Data written to {data_output_dir + data_output_filename}")


# Function to get the latest valid data file, using filename
def get_latest_valid_file(directory):
    """Return the file in a directory with the latest timestamp in the filename."""

    # List the files in the data_read directory
    files_in_directory = os.listdir(directory)

    # Filter for the files that match the expected data filename format,
    # i.e. YYYYMMDD-HHmmss.csv 
    # (adapted from https://stackoverflow.com/a/56223939) 
    # regex reference: https://www.w3schools.com/python/python_regex.asp

    # Search pattern to match valid data files
    search_pattern = r'[0-9]{8}[-][0-9]{6}\.csv$'
    # Create empty list to hold matching filenames
    files_match_pattern= []

    # Iterate through the files in the data_read directory and get the ones with 
    # filenames matching the pattern 
    for file in files_in_directory:
        if re.match(search_pattern, file):
            # If a filename matches the regex string, add it to the new list
            files_match_pattern.append(file)

    # Sort the filtered data files to get the latest one
    latest_filename = sorted(files_match_pattern, reverse=True)[0]

    # Print info for user:
    print(f"Directory {directory} contains {len(files_match_pattern)} files "
        f"with appropriate filenames: the latest one is {latest_filename}.")

    # Return the final data filename
    return(latest_filename)


def read_stock_data_from_csv(file):
    """Read stock data from a CSV file that was written from a yfinance download."""

    # Reading DataFrame from CSV file using pandas.read_csv()
    # (Ref: https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html).
    # Parameters:
    # header=[0,1] - The first two rows of the CSV file contain MultiIndex header information,
    # index_col=0 - I want column 0, the dates, to be the index of the resulting DataFrame,
    # parse_dates=[0] - I want the index values to be parsed as dates (i.e. as datetime objects.)
    # (adapted from https://stackoverflow.com/a/37453925)
    dataframe_read = pd.read_csv(file, header=[0,1], index_col=0, parse_dates=[0])

    # Print info to let the user know what has been done
    print(f"Read in: {file}")

    # Return the new DataFrame
    return dataframe_read


# Function to extract the datetime string from a supplied filename
def remove_filename_extension(file):
    """Removes the extension from a filename. Assumes maximum of 2 period characters in filename."""
    # Split the string at the period character and return the first part.
    string = file.rsplit( ".", 2 )[ 0 ]
    return string


# Function to create PNG plot of supplied data into supplied directory.
def make_png_from_finance_data(dataframe, datetime_string, output_directory):

    # Create figure and matplotlib plots with some additional formatting
    fig, (top, bot) = plt.subplots(2, 1, sharex=True, figsize=(12,8),
                            gridspec_kw=dict(height_ratios=[0.75,0.25]))

    # remove vertical space between subplots
    fig.subplots_adjust(hspace=0)

    # plot Close prices and Volume on separate subplots. 
    # Close prices are plotted without using the datetimes in the data index, i.e. 
    # the periods are plotted all in sequence. 
    # Volume is a stacked bar plot. 
    dataframe["Close"].plot(ax=top, use_index=False)
    dataframe["Volume"].plot(ax=bot, kind='bar', stacked=True, legend=None)

    # set plot title including the timestamp in the name of the read CSV file
    plt.suptitle("Hourly close prices and volume for each stock, " + datetime_string, y=0.93)
    # set labels for x-axis and both y-axes
    bot.set_xlabel("Trading Periods (UTC)")
    bot.set_ylabel("Volume")
    top.set_ylabel("Hourly Close Price ($)")

    # Set fixed major and minor x-tick locations. 
    # Major tick is the start of each trading day at 14:30 UTC. 
    # Minor tick is every other hourly datapoint/  
    ticks_date = dataframe.index.indexer_at_time('14:30')
    ticks_time = np.arange(dataframe.index.size) # step in hours
    top.set_xticks(ticks_date)
    top.set_xticks(ticks_time, minor=True)

    # add vertical gridlines at the start of each day
    top.grid(axis='x', alpha=0.3)

    # set legend location
    top.legend(loc='center right', bbox_to_anchor=(0.8, 0.6))

    # Format major and minor tick labels
    bot.ticklabel_format(axis="y", style="plain")
    bot.tick_params(axis='x', which='minor', labelsize=6, rotation=90)
    labels_date = [maj_tick.strftime('\n%d-%b').replace('\n0', '\n')
                    for maj_tick in dataframe.index[ticks_date]]
    labels_time = [min_tick.strftime('%H:%M')
                    for min_tick in dataframe.index[ticks_time]]
    top.set_xticklabels(labels_date)
    top.set_xticklabels(labels_time, minor=True)
    top.figure.autofmt_xdate(rotation=0, ha='center', which='both')

    # Save plot to file
    plt.savefig(output_directory + datetime_string + ".png")

    # Print message for user
    print(f"Plot created at {output_directory + datetime_string}.png")


def plot_data():
    """Function to open latest data file, plot the Close prices, and save as PNG"""

    # Check if the data directory exists
    check_directory(data_read_dir)

    # Get the filename of the latest valid data file in the data directory 
    data_read_filename = get_latest_valid_file(data_read_dir)

    # Read stock data from csv into dataframe
    df_to_plot = read_stock_data_from_csv(data_read_dir + data_read_filename)

    # Get the timestamp of the data from the CSV filename
    data_timestamp_string = remove_filename_extension(data_read_filename)

    # Create PNG plot of the data
    make_png_from_finance_data(df_to_plot, data_timestamp_string, plot_dir)




# Set list of stock tickers for which we want to download data
tickers = ['META','AAPL','AMZN','NFLX','GOOG']

# Set the directory for the output CSV files.
data_output_dir = "data/"

# Set the directory from which to read CSV files.
data_read_dir = "data/"

# Setting the plot output directory
plot_dir = "plots/"

# Run main functions
get_data()
plot_data()
