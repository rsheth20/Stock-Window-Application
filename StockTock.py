import tkinter as tk
import requests
import json
import random

# Function to make an API request and get the quote data for a new stock
def get_new_quote_data():
    # Select a random symbol from the available traded stocks
    symbol = random.choice(data)['symbol']

    # Make API request to get quote for the symbol
    quote_url = "https://financialmodelingprep.com/api/v3/quote/" + symbol + "API_KEY"
    quote_response = requests.get(quote_url)
    quote_data = quote_response.json()

    # Find the stock in the list of available stocks that matches the selected symbol
    stock_data = next(stock for stock in data if stock['symbol'] == symbol)

    # Get the information for the stock
    name = quote_data[0]["name"]
    price = quote_data[0]["price"]
    dayLow = quote_data[0]["dayLow"]
    dayHigh = quote_data[0]["dayHigh"]
    yearLow = quote_data[0]["yearLow"]
    yearHigh = quote_data[0]["yearHigh"]
    volume = quote_data[0]["volume"]
    avgVolume = quote_data[0]["avgVolume"]
    exchange = stock_data["exchange"]
    exchangeShortName = stock_data["exchangeShortName"]

    # Update the labels with the new quote data
    symbol_label.configure(text="Symbol: " + symbol)
    name_label.configure(text="Name: " + name)
    price_label.configure(text="Price: " + str(price))
    dayLow_label.configure(text="Day Low: " + str(dayLow))
    dayHigh_label.configure(text="Day High: " + str(dayHigh))
    yearLow_label.configure(text="Year Low: " + str(yearLow))
    yearHigh_label.configure(text="Year High: " + str(yearHigh))
    volume_label.configure(text="Volume: " + str(volume))
    avgVolume_label.configure(text="Average Volume: " + str(avgVolume))
    exchange_label.configure(text="Exchange: " + exchange)
    exchangeShortName_label.configure(text="Exchange Short Name: " + exchangeShortName)

# Make initial API request to get list of available traded stocks
url = "https://financialmodelingprep.com/api/v3/available-traded/list?apikey=cf11d6a9d5d03f2ade358f74a882c5c0"
response = requests.get(url)
data = response.json()

# Create the window
window = tk.Tk()
window.title("Stock Tock")

# Add a label for the stock symbol
symbol_label = tk.Label(text="")
symbol_label.pack()

# Add a label for the stock name
name_label = tk.Label(text="")
name_label.pack()

# Add a label for the stock price
price_label = tk.Label(text="")
price_label.pack()

# Add a label for the stock's day low
dayLow_label = tk.Label(text="")
dayLow_label.pack()

# Add a label for the stock's day high
dayHigh_label = tk.Label(text="")
dayHigh_label.pack()

# Add a label for the stock's year low
yearLow_label = tk.Label(text="")
yearLow_label.pack()

# Add a label for the stock's year high
yearHigh_label = tk.Label(text="")
yearHigh_label.pack()

# Add a label for the stock's volume
volume_label = tk.Label(text="")
volume_label.pack()

# Add a label for the stock's average volume
avgVolume_label = tk.Label(text="")
avgVolume_label.pack()

# Add a label for the stock's exchange
exchange_label = tk.Label(text="")
exchange_label.pack()

# Add a label for the stock's exchange short name
exchangeShortName_label = tk.Label(text="")
exchangeShortName_label.pack()

# Add a button to get a new stock quote
next_button = tk.Button(text="Next", command=get_new_quote_data)
next_button.pack()

# Display the initial quote data for a random stock
get_new_quote_data()

# Run the window
window.mainloop()
