import csv
import json
import lxml
from yahooquery import Ticker

# List of tickets to fetch with API
tickets = ["EQNR.OL", "NEL.OL", "DNB.OL", "TEL.OL", "MOWI.OL", "YAR.OL"]

tickets_array = [] 

for ticket in tickets:
    temp_array = [] 
    ticker_obj = Ticker(ticket).price 
    temp_array.append(ticket)
    close = str("%.2f" % ticker_obj[ticket]["regularMarketPreviousClose"])
    temp_array.append(close.replace(".",","))
    temp_array.append(ticker_obj[ticket]["marketCap"]) 
    tickets_array.append(temp_array) 

csv_columns = ['SELSKAP','CLOSE','MARKETCAP']
with open('selskaper.csv', 'w') as csvfile: 
    writer = csv.writer(csvfile, delimiter='\t') 
    writer.writerow(csv_columns)
    for ticket_info in tickets_array: 
            writer.writerow(ticket_info)