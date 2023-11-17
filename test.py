import pandas as pd


df = pd.read_csv('GoogleApps.csv')

# df.info()
print(df['Installs'].median())
# print(df.tail()['Category'])
# print(df.describe())
# print(df['Rating'].median())
# print(df[df['Rating'] > 4.9]['Installs'].mean())
# print(df[(df['Rating'] > 4.9) &(df['Type'] =='Free')]['Installs'].mean())