import pandas as pd
l=[10,20,30,40]
s=pd.Series(l)

print(s)

sd=pd.Series(l,index=['a','b','c','d'])
print('\n')
print(sd)

ind=[1,2,3,4]
s=pd.Series(l,ind)
print(s)