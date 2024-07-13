import pandas as pd
import numpy as np
import array as ar 

arr=ar.array('i',[10,20,30,40])
s=pd.Series(arr)
print(s)
print(arr)

n=np.array([100,200,300,400])
sd=pd.Series(n)
print(sd)
print(n)