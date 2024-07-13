import pandas as pd

d={'name' :['ajay','rahul','rajaji','ganesh','vishal','vishnu'],
   'kom':['76%','75%','67%','56%','89%','92%'],
    'dts':['98%','97%','45%','68%','77%','99%'],
    'entrepreneurship':['99%','76%','68%','45%','43%','98%']}

df=pd.DataFrame(d)

print(df)
print('------------------------------------------')
print(df.head(3))
print('------------------------------------------')
print(df.tail(2))
print('------------------------------------------')
print(df.describe())
print('------------------------------------------')
print(df.shape)
print('------------------------------------------')
print(df.columns)
print('------------------------------------------')
print(df['name'].head())
print('------------------------------------------')
print(df.loc[2])
print('------------------------------------------')
print(df.loc[1:3])
print('------------------------------------------')
for index,row in df.iterrows():
    print(index,row)
print('------------------------------------------')
print(df.loc[df['name']=='ajay'])
