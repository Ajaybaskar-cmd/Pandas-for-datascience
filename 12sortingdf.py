import pandas as pd


d={'name' :['ajay','rahul','rajaji','ganesh','vishal','vishnu'],
   'kom':['76%','75%','67%','56%','89%','92%'],
    'dts':['98%','97%','45%','68%','77%','99%'],
    'entrepreneurship':['99%','76%','68%','45%','43%','98%']}

df=pd.DataFrame(d)
print(df)

print(df.sort_values('name',ascending=0))

print(df.sort_values(['name','entrepreneurship'],ascending=[0,1]))