import numpy as np
import pandas as pd
n_products = 50

# From A to Z are our features
# 100 products. each product has some features,
# of course most of the ti
# mes will be zero because a product just have few features
numpy_serie = np.array(np.random.randint(0, 4, size=(1, 26)))
df_target = pd.DataFrame(numpy_serie, columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), index=['myProduct'])
df_target.index.name = 'productName'

# Featured products
numpy_serie = np.array(np.random.randint(0, 4, size=(99, 26)))
df = pd.DataFrame(numpy_serie, columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))
df['productName'] = pd.util.testing.rands_array(5, 99)
df.set_index('productName', inplace=True)

df = df.append(df_target)
df.to_csv('product_features.csv', index_label=False)

# New product
df_target.to_csv('product.csv', index_label=False)

print(df)
print(df_target)