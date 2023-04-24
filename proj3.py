'''Write a Pandas program to sort a given Series.
400, 300.12,100, 200'''
import pandas as pd
s = pd.Series([400, 300.12,100, 200])
print("Original Data Series:")
print(s)
new_s = pd.Series(s).sort_values()
print(new_s)
