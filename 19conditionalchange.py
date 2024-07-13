import pandas as pd
data={'name':['ajay','ajay','arunkumar','kavinraj','dinesh','tamilselvan','rajaji','saravanan'],
      'tamil':[80,80,70,90,75,56,85,75],
      'english':[56,56,45,75,60,42,67,48],
      'maths':[85,85,67,97,54,48,72,59],
      'science':[54,54,65,89,67,57,91,79],
      'social':[93,93,89,98,78,69,97,79]}

df=pd.DataFrame(data)
print(df)
df['total']=df['tamil']+df['english']+df['maths']+df['science']+df['social']
print(df)

df['percentage']=df['total']/500*100
print(df)

df['grade']='none'

print(df)

"""
less than 40 =fail
>40 and <60  pass
>60 and <70  first class
>70 distinction
    
"""

print('----------------------------------------------------------------')

df.loc[df['percentage']<40,['grade']]='fail'
print(df)
df.loc[(df['percentage']>40) & (df['percentage']<60),['grade']]='pass'
print(df)

df.loc[(df['percentage']>60) & (df['percentage']<70),['grade']]='First class'
df.loc[(df['percentage']>70),['grade']]='Distinction'
print(df)
 