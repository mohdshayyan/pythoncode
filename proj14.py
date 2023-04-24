'''Write a Pandas program to combining two series into a DataFrame.'''
import pandas as pd
import numpy as np
s1 = pd.Series(['100', '200', '400'])
s2 = pd.Series(['10', '20', '40'])
print("Data Series:")
print(s1)
print(s2)
df = pd.concat([s1, s2], axis=1)
print("New DataFrame combining two series:")
print(df)
