import pandas as pd


def based_on_corr(ratings_df, products_df, n, id):
    """
    Normally people rated what they like or dislike.
    Count votes is a way of knowing what they really like or dislike
    """
    ratings_pivot = pd.pivot_table(data=ratings_df, values='rating', index='userID', columns='productID')
    pearson = ratings_pivot.corrwith(ratings_pivot[id])

    similar_products = pd.DataFrame(pearson, columns=['Pearson_Corr'])
    similar_products.dropna(inplace=True)

    similar_products_desc = similar_products.sort_values('Pearson_Corr', ascending=False)
    most_valued = similar_products_desc.head(n).index.tolist()

    return products_df[products_df['productID'].isin(most_valued)]


def main():
    n = 5
    id = 2
    ratings_df = pd.read_csv('product_ratings.csv')
    products_df = pd.read_csv('product_list.csv')

    print(based_on_corr(ratings_df, products_df, n, id))

if __name__ == "__main__":
    main()
