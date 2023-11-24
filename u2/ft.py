import pandas as pd
df = pd.read_csv('GoogleApps.csv')
# 1 задание: во сколько раз количество приложений для аудитории «все пользователи»  превышает количество приложения для пользователей «старше 10 лет»? 
Everyone = df[(df['Content Rating'] == 'Everyone')] ['Content Rating'].count()
Everyone10 = df[(df['Content Rating'] == 'Everyone 10+')] ['Content Rating'].count()
print('Соотношение приложений для всех и для детей:', Everyone/Everyone10)


# 2 задание: чему равен средний размер приложений для каждой целевой аудитории?
print('Средний размер приложений для аудитории Everyone:', df[df['Content Rating'] == 'Everyone']['Size'].mean())
print('Средний размер приложений для аудитории Everyone 10+:', df[df['Content Rating'] == 'Everyone 10+']['Size'].mean())
print('Средний размер приложений для аудитории Teen:', df[df['Content Rating'] == 'Teen']['Size'].mean())


# 3 задание: чему равен минимальный и максимальный размер платных и бесплатных приложений для каждой целевой аудитории? #Обозначения: а) целевой аудитории E10 - Everyone 10+; E - Everyone; T -Teen б) тип приложения F- бесплатное; P - платное.


E10_min_F = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Free')] ['Size'].min()
E_min_F = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Free')] ['Size'].min()
T_min_F = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Free')] ['Size'].min()
E10_min_F = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Free')] ['Size'].min()
E_min_F = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Free')] ['Size'].min()
T_min_F = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Free')] ['Size'].min()
E10_max_F = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Free')] ['Size'].max()
E_max_F = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Free')] ['Size'].max()
T_max_F = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Free')] ['Size'].max()
E10_min_P = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Paid')] ['Size'].min()
E_min_P = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Paid')] ['Size'].min()
T_min_P = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Paid')] ['Size'].min()
E10_max_P = df[(df['Content Rating'] == 'Everyone 10+') & (df['Type'] =='Paid')] ['Size'].max()
E_max_P = df[(df['Content Rating'] == 'Everyone') & (df['Type'] =='Paid')] ['Size'].max()
T_max_P = df[(df['Content Rating'] == 'Teen') & (df['Type'] =='Paid')] ['Size'].max()
print('Минимальный размер бесплатных приложений:', 'E10 =', E10_min_F, ';',  'E =', E_min_F, ';',  'T =', T_min_F)
print('Максимальный размер бесплатных приложений:', 'E10 =', E10_max_F, ';',  'E =', E_max_F, ';',  'T =', T_max_F)
print('Минимальный размер платных приложений:', 'E10 =', E10_min_P, ';',  'E =', E_min_P, ';',  'T =', T_min_P)
print('Максимальный размер платных приложений:', 'E10 =', E10_max_P, ';',  'E =', E_max_P, ';',  'T =', T_max_P)
