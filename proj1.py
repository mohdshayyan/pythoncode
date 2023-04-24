'''Write a Pandas program to multiple and divide two Pandas Series.
Sample Series: [2, 4, 8, 10], [1, 3, 7, 9]'''
import pandas as pd
ds1 = pd.Series([2, 4, 8, 10])
ds2 = pd.Series([1, 3, 7, 9])
print("Multiply two Series:")
ds = ds1 * ds2
print(ds)
print("Divide Series1 by Series2:")
ds = ds1 / ds2
print(ds)
