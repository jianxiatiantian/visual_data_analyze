import pandas as pd
import numpy as np
s1 = pd.Series([1,2,3,np.nan,'a'])
s2 = pd.Series([1,2,3,4,5,6],index=['A','B','C','D','E','F'])
print(s1.values)
print(s1.index)
print(s1)
print(s2.values)
print(s2.index)
print(s2)
print(s2['A':'D'])
