import pandas as pd
di={'name':['ajay','ganesh','rahul'],
    'branch':['mech','cse','it']}

ind=[1,2,3]

df=pd.DataFrame(di,index=ind)
print(df)