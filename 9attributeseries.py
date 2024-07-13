import pandas as pd
s=pd.Series([10,20,30,40,50,60],index=['a','b','c','d','e','f'],name='ajay')

print(s.index)
print(s.array)
print(s.values)
print(s.name)
print(s.shape)
print(s.ndim)
print(s.size)
print(s.nbytes)
print(s.memory_usage(index=0))
print(s.empty)

s1=pd.Series()
print(s1.empty)