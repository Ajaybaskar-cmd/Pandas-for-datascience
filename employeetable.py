import pandas as pd
data=pd.read_csv("F:\\csv file\\Employee.csv")
df=pd.DataFrame(data)
print(df)

print(df.tail())

print(df.loc[df['Gender'].str.startswith('F')].head())