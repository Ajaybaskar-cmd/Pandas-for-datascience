import pandas as pd

data={'name':['ajay','arunkumar','kavinraj','dinesh','tamilselvan','rajaji','saravanan'],
      'tamil':[80,70,90,75,56,85,75],
      'english':[56,45,75,60,42,67,48],
      'maths':[85,67,97,54,48,72,59],
      'science':[54,65,89,67,57,91,79],
      'social':[93,89,98,78,69,97,79]}

df=pd.DataFrame(data)
print(df)
df["total_marks"]=0
print(df)

df['total_marks']=df['tamil']+df['english']+df['maths']+df['science']+df['social']
print(df)

df=df.drop(['tamil'],axis=1)
print(df)