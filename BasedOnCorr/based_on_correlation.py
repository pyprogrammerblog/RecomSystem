import pandas as pd


def based_on_corr(ratings_df, products_df, name, number):
    """
    Normally people rated what they like or dislike.
    Count votes is a way of knowing what they really like or dislike
    """
    # Utility  1000x50  1000 people x 50 product
    ratings_pivot = pd.pivot_table(
        data=ratings_df,
        values='rating',
        index='userID',
        columns='productID'
    )

    # first get id for a product.
    index_column = products_df[products_df['productName'] == name].index[0]

    # then vector of correlation for this product respect to the rest of products
    pearson = ratings_pivot.corrwith(ratings_pivot[index_column])

    # make a dataframe. Index is keeping same order than productID so concat
    similar_products = pd.DataFrame(pearson, columns=['Pearson_Corr'])
    similar_products.dropna(inplace=True)
    similar_products = similar_products.sort_values('Pearson_Corr', ascending=False)

    most_valued = similar_products.head(number).index.tolist()

    return products_df.loc[most_valued]


def main():
    number = 5
    name = 'Zj8xzeYHTC'
    ratings_df = pd.read_csv('product_ratings.csv')
    products_df = pd.read_csv('product_list.csv')

    print(based_on_corr(ratings_df, products_df, name, number))

if __name__ == "__main__":
    main()
