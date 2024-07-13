import pandas as pd

data={'name':['ajay','ajay','arunkumar','kavinraj','dinesh','tamilselvan','rajaji','saravanan'],
      'tamil':[80,80,70,90,75,56,85,75],
      'english':[56,56,45,75,60,42,67,48],
      'maths':[85,85,67,97,54,48,72,59],
      'science':[54,54,65,89,67,57,91,79],
      'social':[93,93,89,98,78,69,97,79]}

df=pd.DataFrame(data)
print(df)

print(df.duplicated())

print(df.drop_duplicates())
print(df)

df.drop_duplicates(inplace=True)
print(df)