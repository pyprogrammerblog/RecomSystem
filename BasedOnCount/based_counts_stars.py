import pandas as pd

# get data
ratings_df = pd.read_csv('product_ratings.csv')
products_df = pd.read_csv('product_list.csv')

# group by and count
counts_df = pd.DataFrame(ratings_df.groupby('productID', as_index=False)['rating'].count())
counts_df = counts_df.sort_values('rating', ascending=False)

# filter and return most valued product
most_valued = counts_df.head(5)['productID'].tolist()

print(products_df[products_df['productID'].isin(most_valued)])

