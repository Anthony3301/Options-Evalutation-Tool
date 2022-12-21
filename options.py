import numpy as np
import pandas as pd
import yfinance as yf
import json as js

# Function to pull option information of a stock
def option_pull(sym):
    ticker = yf.Ticker(sym)
    list_of_expirations = ticker.options

    # dataframe for options
    options = pd.DataFrame()

    for entry in list_of_expirations:
        curr_option = ticker.option_chain(entry)
        aggr_option = pd.DataFrame().append(curr_option.calls).append(curr_option.puts)
        aggr_option['expirationDate'] = entry
        options = options.append(aggr_option, ignore_index=True)

    return options

print (option_pull("AMD"))





