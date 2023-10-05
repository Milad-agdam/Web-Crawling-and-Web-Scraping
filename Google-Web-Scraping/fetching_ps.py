from take_post_code import post_cart
import pandas as pd
from connect_to_driver import my_driver
city = ['London', 'Birmingham', 'Newcastle', 'Glasgow', 'Edinburgh', 'Dunfermline', 'Livingston', 'Bathgate', 'Paisley', 'Aberdeen']

a = ['Aberdeen']
cities = []


for i in a:
    post_codes = post_cart(i)
    for j in range(len(post_codes)):
        cities.append(i)


df = pd.DataFrame({'city': cities, "post_codes": post_codes})

print(df)
df.to_excel('Output.xlsx', sheet_name='Sheet2')
