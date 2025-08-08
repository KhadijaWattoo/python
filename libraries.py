import numpy as np
import pandas as pd

# Create a NumPy array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print("NumPy Array:")
print(arr)

# Create a Pandas DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [30, 25, 35],
    'Score': [85, 90, 95],
    'Number': [3210,3220,89]
}
df = pd.DataFrame(data)

print("\nPandas DataFrame:")
print(df)

# Calculate the mean age
mean_age = df['Age'].mean()
print(f"\nAverage Age: {mean_age}")