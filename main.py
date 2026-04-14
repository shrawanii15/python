import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

# a) Print complete report
print("\n----- Complete Book Report -----")
print(df)

# b) Books by given author
author = input("\nEnter author name: ")
print("\nBooks by", author)
print(df[df["Author"] == author])

# c) Books by given publisher
publisher = input("\nEnter publisher name: ")
print("\nBooks by Publisher:", publisher)
print(df[df["Publisher"] == publisher])

# d) Cheapest and costliest book
print("\nCheapest Book:")
print(df[df["Price"] == df["Price"].min()][["Title","Price"]])

print("\nCostliest Book:")
print(df[df["Price"] == df["Price"].max()][["Title","Price"]])

# e) Sort by year
print("\nBooks sorted by Year:")
print(df.sort_values(by="Year"))