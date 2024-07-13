import pandas as pd
d={'a':10,'b':20,'c':30}

s=pd.Series(d)
print(s)

d={'a':[10,20],'b':[30,40],'c':[50,60]}
sd=pd.Series(d)
print(sd)

di=(('a',10),('b',20))
s=pd.Series(di)
print(s)