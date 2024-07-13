import pandas as pd
data={'name':['ajay','ajay','arunkumar','kavinraj','dinesh','tamilselvan','rajaji','saravanan'],
      'tamil':[80,80,70,90,75,56,85,75],
      'english':[56,56,45,75,60,42,67,48],
      'maths':[85,85,67,97,54,48,72,59],
      'science':[54,54,65,89,67,57,91,79],
      'social':[93,93,89,98,78,69,97,79]}


df=pd.DataFrame(data)
print(df)
print("----------------------------------------------------------------")

print(df.loc[df['tamil']<60])
print("-------------------------------------------------------------------")

#numerical condition
#and conditon
print(df.loc[(df['tamil']>60) & (df['english']<60)])

print("--------------------------------------------------------")
#or condition

print(df.loc[(df['tamil']<60) | (df['english']<60)])

print("-------------------------------------------------------------")
#not condition
print(df.loc[~(df['tamil']<60)])

print("-------------------------------------------------------------------")
#string condition
#str.contains   condtion
print(df.loc[(df["name"].str.contains("y"))])
print("----------------------------------------------------------------")
#not condition
print(df.loc[~df['name'].str.contains('y')])

#str.startswith condition
print(df.loc[df['name'].str.startswith('a')])

print(df.loc[df['name'].str.endswith('y')])

print(df.drop_duplicates())