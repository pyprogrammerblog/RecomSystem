import numpy as np
import pandas as pd

n_products = 50
n_people = 1000

df = pd.DataFrame()
df['userID'] = np.random.randint(0, n_people, size=10000)  # 1000 people
df['productID'] = np.random.randint(0, n_products, size=df.userID.size)  # 50 products
df['rating'] = np.random.randint(1, 4, size=df.userID.size)  # rating from 1-4

s = df.drop_duplicates(subset=['userID', 'productID'])
print('Everything ok' if not any(s.duplicated(subset=['userID', 'productID'])) else 'Something wrong')

if not any(s.duplicated(subset=['userID', 'productID'])):
    s.to_csv('product_ratings.csv', index_label=False)

df2 = pd.DataFrame()
df2['productName'] = pd.util.testing.rands_array(10, n_products)
df2.to_csv('product_list.csv', index_label=False)

print(df)
print(df2)