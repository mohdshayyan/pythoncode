'''Write a Pandas program to change the order of index of a given
series.
Original Data Series:
A 1
B 2
C 3
dtype: int64
Data Series after changing the order of index:
B 2
A 1
C 3
dtype: int64'''
import pandas as pd
s = pd.Series(data = [1,2,3], index = ['A', 'B', 'C'])
print("Original Data Series:")
print(s)
s = s.reindex(index = ['B','A','C'])
print("Data Series after changing the order of index:")
print(s)
