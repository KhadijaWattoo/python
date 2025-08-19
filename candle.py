import pandas as pd
import mplfinance as mpf

# Path to the CSV file
file_path = r"C:\Users\HP i5\Downloads\goldstock v1.csv"

# Read the CSV file
df = pd.read_csv(file_path)

# Display first few rows
print(df.head())

# --- PROCESSING ---

# Convert 'Date' to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Filter data for the years 2022 and 2023
df = df[(df['Date'].dt.year >= 2022) & (df['Date'].dt.year <= 2023)]

# Sort by date
df = df.sort_values('Date')

# Set Date as index (required for mplfinance)
df.set_index('Date', inplace=True)

# Calculate the 7, 50, and 100 day moving averages
df['7_day_MA'] = df['Close'].rolling(window=7).mean()
df['50_day_MA'] = df['Close'].rolling(window=50).mean()
df['100_day_MA'] = df['Close'].rolling(window=100).mean()

# --- PLOTTING ---

# Prepare the moving averages for mplfinance
ma7 = mpf.make_addplot(df['7_day_MA'], color='orange')
ma50 = mpf.make_addplot(df['50_day_MA'], color='green')
ma100 = mpf.make_addplot(df['100_day_MA'], color='blue')

# Plot the candlestick chart with moving averages
mpf.plot(df, type='candlestick', style='charles', title="Candlestick Chart with Moving Averages (2022-2023)",
         ylabel="Price", addplot=[ma7, ma50, ma100], figsize=(14, 7))
