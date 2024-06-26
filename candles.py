# Install necessary libraries if not already installed
# !pip install matplotlib pandas fyers-apiv2

import matplotlib.pyplot as plt
import pandas as pd
import os
from fyers_api import fyersModel

# Replace with your actual client ID and access token
client_id = "2A6LCH4LF8-100"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MTkzODEwNDMsImV4cCI6MTcxOTQ0ODI0MywibmJmIjoxNzE5MzgxMDQzLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCbWU2d3pYTWdfalBvSXUtOVFhR0RndC04WlBIZ2tfYnpCRi1EcTB3WUFvUFFrU1JmWkJYd3dPbHloekJsdU9YR09qX2lKWTVOaWtESGpnQUd3c2taSjQ0WlVqY2NkaXBMRFJZc08yZFJvc3dYdHNEcz0iLCJkaXNwbGF5X25hbWUiOiJQUklZQU5LQSBHVVBUQSIsIm9tcyI6IksxIiwiaHNtX2tleSI6IjdhYjY3OTI0NzQ5MDY0Y2E0MmEzOWExNmU0MmIxOTJmY2Q0NTlkZDhlNWU5MDZhMmQ5NzVkNTk4IiwiZnlfaWQiOiJZUDExMjYzIiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.NImvNXjlj9YZPZfUS3PYzP0N9Q0KLlR_9QduqGt0Zoc"

log_path = os.path.join(os.getcwd(), "fyers_logs")

# Create the directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path=log_path)

# Define the data for the API request
data = {
    "symbol": "NSE:SBIN-EQ",
    "resolution": "D",
    "date_format": "0",
    "range_from": "1690895316",
    "range_to": "1691068173",
    "cont_flag": "1"
}

# Fetch the historical data
response = fyers.history(data=data)
print(response)

# Check if the response is successful
if response['s'] == 'ok':
    # Extract the candle data
    candles = response['candles']
    
    # Convert the response data to a DataFrame
    columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
    df = pd.DataFrame(candles, columns=columns)
    
    # Convert timestamp to datetime
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
    
    # Convert range_from and range_to to numeric before converting to datetime
    range_from = pd.to_numeric(data["range_from"])
    range_to = pd.to_numeric(data["range_to"])
    
    # Plotting the candlestick chart
    fig, ax = plt.subplots(figsize=(10, 5))
    
    for index, row in df.iterrows():
        color = 'green' if row['close'] >= row['open'] else 'red'
        ax.plot([row['timestamp'], row['timestamp']], [row['low'], row['high']], color='black')
        ax.plot([row['timestamp'], row['timestamp']], [row['open'], row['close']], color=color, linewidth=5)
    
    # Add additional details to the title
    ax.set_title(f'Candlestick Chart for {data["symbol"]} \nDate Range: {pd.to_datetime(range_from, unit="s").strftime("%Y-%m-%d")} to {pd.to_datetime(range_to, unit="s").strftime("%Y-%m-%d")}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Price')
    ax.grid(True)
    
    plt.show()
else:
    print("Failed to fetch data:", response)

