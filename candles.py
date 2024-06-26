# Install necessary libraries if not already installed
# !pip install matplotlib pandas fyers-apiv2

import matplotlib.pyplot as plt
import pandas as pd
import os
from fyers_api import fyersModel

# Replace with your actual client ID and access token
client_id = "2A6LCH4LF8-100"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.********.NImvNXjlj9YZPZfUS3PYzP0N9Q0KLlR_9QduqGt0Zoc"

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
    
    # Plotting the candlestick chart with volume
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})
    
    # Plotting the candlestick chart
    for index, row in df.iterrows():
        color = 'green' if row['close'] >= row['open'] else 'red'
        ax1.plot([row['timestamp'], row['timestamp']], [row['low'], row['high']], color='black')
        ax1.plot([row['timestamp'], row['timestamp']], [row['open'], row['close']], color=color, linewidth=5)
    
    # Plotting the volume chart
    ax2.bar(df['timestamp'], df['volume'], color='blue', alpha=0.6)
    
    # Add additional details to the title
    ax1.set_title(f'Candlestick Chart for {data["symbol"]} \nDate Range: {pd.to_datetime(range_from, unit="s").strftime("%Y-%m-%d")} to {pd.to_datetime(range_to, unit="s").strftime("%Y-%m-%d")}')
    ax1.set_ylabel('Price')
    ax2.set_ylabel('Volume')
    ax2.set_xlabel('Date')
    
    ax1.grid(True)
    ax2.grid(True)
    
    plt.show()
else:
    print("Failed to fetch data:", response)
