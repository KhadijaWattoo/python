
# import pandas as pd
# import matplotlib.pyplot as plt
# file_path = r"C:\Users\HP i5\Downloads\average-rainfall-temperature-1.csv"  # Update this path
# df = pd.read_csv(file_path)
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
# mean_values = df.mean(numeric_only=True)
# mode_values = df.mode(numeric_only=True).iloc[0]   
# std_dev_values = df.std(numeric_only=True)   
# variance_values = df.var(numeric_only=True)  
# min_values = df.min(numeric_only=True)   
# max_values = df.max(numeric_only=True)
 
# print("Mean of numeric columns:\n", mean_values)
# print("Mode values:\n", mode_values, "\n")
# print("Standard Deviation:\n", std_dev_values, "\n")
# print("Variance:\n", variance_values, "\n")
# print("Minimum values:\n", min_values, "\n")
# print("Maximum values:\n", max_values, "\n")
# print(df)
# import pandas as pd
# import matplotlib.pyplot as plt

 
# file_path = r"C:\Users\HP i5\Downloads\average-rainfall-temperature-1.csv"  # Update this path
 
# df = pd.read_csv(file_path)

 
# df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

 
# numeric_cols = df.select_dtypes(include=['number'])

 
# mean_values = numeric_cols.mean()
# median_values = numeric_cols.median()
# mode_values = numeric_cols.mode().iloc[0]   
# std_dev_values = numeric_cols.std()   
# variance_values = numeric_cols.var()   
# min_values = numeric_cols.min()   
# max_values = numeric_cols.max()  

 
# stats_df = pd.DataFrame({
#     "Mean": mean_values,
#     "Median": median_values,
#     "Mode": mode_values,
#     "Std Dev": std_dev_values,
#     "Variance": variance_values,
#     "Min": min_values,
#     "Max": max_values
# })

 
# fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))   

 
# for column in numeric_cols.columns:
#     axes[0].plot(numeric_cols.index, numeric_cols[column], label=column)

# axes[0].set_title("Line Chart of Entire Dataset")
# axes[0].set_xlabel("Index")
# axes[0].set_ylabel("Values")
# axes[0].legend()
# axes[0].grid(True)

 
# for column in stats_df.columns:
#     axes[1].plot(stats_df.index, stats_df[column], label=column, marker='o')

# axes[1].set_title("Statistical Summary (Mean, Median, Mode, Std Dev, Variance, Min, Max)")
# axes[1].set_xlabel("Columns")
# axes[1].set_ylabel("Values")
# axes[1].set_xticklabels(stats_df.index, rotation=90)  
# axes[1].legend()
# axes[1].grid(True)

 
# plt.tight_layout()
# plt.show()
import pandas as pd
import matplotlib.pyplot as plt

# ✅ Step 1: Define file path
file_path = r"C:\Users\HP i5\Downloads\average-rainfall-temperature-1.csv"  # Update this path

# ✅ Step 2: Read CSV file
df = pd.read_csv(file_path)

# ✅ Step 3: Remove "Unnamed" columns
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]

# ✅ Step 4: Select numeric columns
numeric_cols = df.select_dtypes(include=['number'])

# ✅ Step 5: Calculate 7-Day Moving Average
moving_avg = numeric_cols.rolling(window=7).mean()

# ✅ Step 6: Calculate Statistics
mean_values = numeric_cols.mean()
median_values = numeric_cols.median()
mode_values = numeric_cols.mode().iloc[0]  # First mode value
std_dev_values = numeric_cols.std()  # Standard Deviation
variance_values = numeric_cols.var()  # Variance
min_values = numeric_cols.min()  # Minimum values
max_values = numeric_cols.max()  # Maximum values

# ✅ Step 7: Create a DataFrame for statistical values
stats_df = pd.DataFrame({
    "Mean": mean_values,
    "Median": median_values,
    "Mode": mode_values,
    "Std Dev": std_dev_values,
    "Variance": variance_values,
    "Min": min_values,
    "Max": max_values
})

 
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(12, 12))  # 2 Rows, 1 Column

 
for column in numeric_cols.columns:
    axes[0].plot(numeric_cols.index, numeric_cols[column], label=f"Original {column}")
    axes[0].plot(moving_avg.index, moving_avg[column], linestyle="dashed", label=f"21-Day MA {column}")

axes[0].set_title("Line Chart of Entire Dataset + 21-Day Moving Average")
axes[0].set_xlabel("Index")
axes[0].set_ylabel("Values")
axes[0].legend()
axes[0].grid(True)

 
for column in stats_df.columns:
    axes[1].plot(stats_df.index, stats_df[column], label=column, marker='o')

axes[1].set_title("Statistical Summary (Mean, Median, Mode, Std Dev, Variance, Min, Max)")
axes[1].set_xlabel("Columns")
axes[1].set_ylabel("Values")
axes[1].set_xticklabels(stats_df.index, rotation=90)  # Rotate x-axis labels
axes[1].legend()
axes[1].grid(True)

 
plt.tight_layout()
plt.show()

