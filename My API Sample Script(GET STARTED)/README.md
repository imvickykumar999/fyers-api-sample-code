## Given the rate limits:

- **Per Second**: 10 requests
- **Per Minute**: 200 requests
- **Per Day**: 10,000 requests

![image](https://github.com/imvickykumar999/fyers-api-sample-code/assets/50515418/945d58aa-9e45-4f66-97e1-73bd6eeb68fb)

To avoid hitting the rate limits while updating the plot as frequently as possible, we need to find a balance. 

### Calculation:
1. **Per Second**: The maximum is 10 requests per second. If we set `interval=1000` (1 second), we would be making 1 request per second, which is safe.
2. **Per Minute**: The maximum is 200 requests per minute. If we set `interval=1000` (1 second), this would result in 60 requests per minute, which is well within the limit.
3. **Per Day**: The maximum is 10,000 requests per day. If we set `interval=1000` (1 second), this would result in 60 * 60 * 24 = 86,400 requests per day, which exceeds the limit.

To avoid exceeding the daily limit, we need to adjust the interval to a value that keeps us within the daily limit.

### Adjusting for Daily Limit:
To stay within the 10,000 requests per day limit, we can calculate the appropriate interval:
\[ \text{Seconds per day} = 86400 \]
\[ \text{Allowed requests per day} = 10000 \]
\[ \text{Minimum interval} = \frac{86400}{10000} = 8.64 \text{ seconds} \]

Rounding up, we should set the interval to 9 seconds.

### Updated Code:
Here’s the updated code with the interval set to 9000 milliseconds (9 seconds):

```python
# Install necessary libraries if not already installed
# !pip install matplotlib pandas fyers-apiv2

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
import os
import time
from datetime import datetime, timedelta
from fyers_api import fyersModel
from matplotlib.animation import FuncAnimation

# Replace with your actual client ID and access token
client_id = "2A6LCH4LF8-100"
access_token = "your_access_token_here"  # Make sure to replace with your actual access token

log_path = os.path.join(os.getcwd(), "fyers_logs")

# Create the directory if it doesn't exist
os.makedirs(log_path, exist_ok=True)

# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, is_async=False, token=access_token, log_path=log_path)

# Define the date range for the last one year
end_date = datetime.now()
start_date = end_date - timedelta(days=300)

# Convert the date range to Unix timestamps
range_from = int(start_date.timestamp())
range_to = int(end_date.timestamp())

# Define the data for the API request
data = {
    "symbol": "NSE:GTLINFRA-EQ",
    "resolution": "D",
    "date_format": "0",
    "range_from": str(range_from),
    "range_to": str(range_to),
    "cont_flag": "1"
}

# Initialize the plot
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True, gridspec_kw={'height_ratios': [3, 1]})

# Function to fetch data and update the plot
def update(frame):
    global range_to
    range_to = int(datetime.now().timestamp())
    data["range_to"] = str(range_to)
    
    response = fyers.history(data=data)
    if response['s'] == 'ok':
        candles = response['candles']
        columns = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
        df = pd.DataFrame(candles, columns=columns)
        df['timestamp'] = pd.to_datetime(df['timestamp'], unit='s')
        
        ax1.clear()
        ax2.clear()
        
        for index, row in df.iterrows():
            color = 'green' if row['close'] >= row['open'] else 'red'
            ax1.plot([row['timestamp'], row['timestamp']], [row['low'], row['high']], color='black')
            ax1.plot([row['timestamp'], row['timestamp']], [row['open'], row['close']], color=color, linewidth=5)
        
        ax2.bar(df['timestamp'], df['volume'], color='blue', alpha=0.6)
        
        ax1.set_title(f'Candlestick Chart for {data["symbol"]}')
        ax1.set_ylabel('Price')
        ax2.set_ylabel('Volume')
        ax2.set_xlabel('Date')
        
        ax1.grid(True)
        ax2.grid(True)
        plt.xticks(rotation=45)
    else:
        print("Failed to fetch data:", response)

# Create an animation
ani = FuncAnimation(fig, update, interval=9000, cache_frame_data=False)  # Update every 9 seconds

plt.show()
```

### Explanation:
1. **Interval**: Set to `9000` milliseconds (9 seconds) to stay within the daily request limit.
2. **API Call Frequency**: This will make approximately 9,600 requests per day, which is under the 10,000 request limit and respects the per second and per minute limits.

---

To understand the difference between a **limit order** and a **stop order**, especially in the context of prioritizing price over the speed of execution, let's delve into their definitions and functionalities:

### Limit Order

**Definition**: A limit order is an order to buy or sell a security at a specific price or better.

**Key Characteristics**:
- **Price Control**: Ensures the order will only be executed at the specified limit price or a better price (lower for buy orders, higher for sell orders).
- **Execution**: Not guaranteed to be executed if the market price does not reach the limit price. The priority is on the price, not the speed of execution.
- **Use Case**: Useful when you want to ensure that you do not pay more (for a buy) or receive less (for a sell) than the desired price. Suitable for less liquid stocks or when you have a specific target price in mind.

**Example**:
- You place a limit order to buy 100 shares at $45. The order will only execute if the stock price drops to $45 or lower. If the stock does not reach $45, the order remains unfilled.

### Stop Order (Stop-Loss Order)

**Definition**: A stop order becomes a market order once the stop price is reached. It is primarily used to limit losses or protect profits.

**Key Characteristics**:
- **Trigger Price**: The order is inactive until the stop price is reached. Once the stop price is hit, it becomes a market order and executes at the best available price.
- **Execution**: Execution is guaranteed once the stop price is reached, but the price at which it executes can be different from the stop price due to market conditions. The priority is on execution speed once triggered.
- **Use Case**: Useful for protecting against significant losses or locking in profits. Commonly used in volatile markets where price movements can be swift and substantial.

**Example**:
- You own a stock currently trading at $50. You place a stop order to sell if the price drops to $45. If the price hits $45, the order converts to a market order and will sell at the next available price, which could be slightly above or below $45.

### Comparison in Terms of Price Priority and Speed

- **Limit Order**: 
  - **Price Priority**: High. The order will only execute at the specified limit price or better.
  - **Speed of Execution**: Low. Execution is not guaranteed if the price does not reach the limit.

- **Stop Order**: 
  - **Price Priority**: Low. Once the stop price is hit, the execution price can vary.
  - **Speed of Execution**: High. Converts to a market order and executes immediately once triggered.

### Example to Highlight Differences

Suppose you own a stock currently trading at $50:
- **Limit Order**:
  - You set a **sell limit order** at $55. The stock must rise to $55 for the order to execute. If it never reaches $55, the order remains unfilled. Here, the priority is getting the price you want ($55) rather than how quickly the order executes.

- **Stop Order**:
  - You set a **sell stop order** at $45. If the stock price falls to $45, the order becomes a market order and sells at the next available price. This might be $44.90 or $44.50 depending on market conditions at the time. Here, the priority is on executing the order quickly to prevent further losses, rather than the exact price.

### Summary

- **Limit Order**: Prioritizes price over speed. It is ideal when you have a target price and can wait for the market to reach it.
- **Stop Order**: Prioritizes speed over price. It is ideal for protecting against significant losses by triggering a market order once the stop price is reached.

For further reading, you can refer to:
1. [Investopedia - Limit Order](https://www.investopedia.com/terms/l/limitorder.asp)
2. [Investopedia - Stop Order](https://www.investopedia.com/terms/s/stoporder.asp)
