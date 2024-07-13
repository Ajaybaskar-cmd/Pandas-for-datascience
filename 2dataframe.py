import pandas as pd
d={'Name':['ajay','rahul','ganesh'],'percentage':[97,98,99]}

print(pd.DataFrame(d))
Df=pd.DataFrame(d)
print(Df)

print(Df.describe())
print(Df.shape)