import pandas as pd

df = pd.read_csv('BasicStats/Housing.csv')

print(f"this is mean of prices in housing data: {df['price'].mean()}")
print(f"this is mode of prices in housing data: {df['price'].mode()}")
print(f"this is median of prices in housing data: {df['price'].median()}")
print(f"this is the minimum price in housing data: {df['price'].min()}")
print(f"this is the maximum price in housing data: {df['price'].max()}")
