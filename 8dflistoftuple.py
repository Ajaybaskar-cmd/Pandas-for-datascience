import pandas as pd
t=[('ajay','mech',97),('rahul','cse',98),('ganesh','it',99)]

df=pd.DataFrame(t,columns=['name','branch','perc'])
print(df)