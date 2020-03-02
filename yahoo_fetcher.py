import csv
import json
import lxml
import yfinance as yf

# List of tickets to fetch with API
tickets = ["EQNR", "GOOG"]

tickets_array = [] # List to put array

# Looping over tickets and fetch each ticket info into temp_array
for ticket in tickets:
    temp_array = [] # Temporary array
    ticker = yf.Ticker(ticket) # Initlize ticket class
    temp_array.append(ticket) # Add ticket name to temp_array
    temp_array.append(ticker.info["previousClose"]) # Add ticket CLOSE to temp_array
    temp_array.append(ticker.info["marketCap"]) # Add ticket MARKETCAP to temp_array
    tickets_array.append(temp_array) # Add temp_array to tickets array

# Write results to file with head csv_columns
csv_columns = ['SELSKAP','CLOSE','MARKETCAP'] # Header
with open('selskaper.csv', 'w') as csvfile: # Open file
    writer = csv.writer(csvfile, delimiter=',') # Write to file with delimiter '|' (pipe)
    writer.writerow(csv_columns)
    # Loop over tickets in tickets_array and write row to file
    for ticket_info in tickets_array: 
            writer.writerow(ticket_info)
