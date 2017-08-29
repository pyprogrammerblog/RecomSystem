import numpy as np
import pandas as pd
n_products = 5000

# Featured products
numpy_serie = np.array(np.random.randint(0, 2, size=(n_products, 26)))
df = pd.DataFrame(numpy_serie, columns=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

# New product
df.to_csv('product_features.csv', index_label=False)

# New product
numpy_serie = np.array(np.random.randint(0, 2, size=(1, 25)))
df_target = pd.DataFrame(numpy_serie, columns=list('ABCDEFGHIJKLMNOPQRSTUVWXY'))
df_target.to_csv('product.csv', index_label=False)

print(df)
print(df_target)