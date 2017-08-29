import pandas as pd


def based_on_count(ratings_df, products_df, n):
    """
    Based on count
    """
    # group by and count
    counts_df = pd.DataFrame(ratings_df.groupby('productID')['rating'].count())
    counts_ascending_df = counts_df.sort_values('rating', ascending=False)

    # filter and return most valued product
    most_valued = counts_ascending_df.head(n).index.tolist()

    return products_df.loc[most_valued]


def based_on_mean(ratings_df, products_df, n):
    """
    Based on mean
    """
    # group by and count
    counts_df = pd.DataFrame(ratings_df.groupby('productID')['rating'].count())
    counts_df['rating_avg'] = pd.DataFrame(ratings_df.groupby('productID')['rating'].mean())
    counts_avg_df = counts_df.sort_values('rating_avg', ascending=False)

    # # filter and return most valued product
    most_valued = counts_avg_df.head(n).index.tolist()

    return products_df.loc[most_valued]


def main():

    # inputs
    n = 5
    ratings_df = pd.read_csv('product_ratings.csv')
    products_df = pd.read_csv('product_list.csv')

    # calculating
    print('Based on counts')
    print(based_on_count(ratings_df, products_df, n))
    print('Based on mean')
    print(based_on_mean(ratings_df, products_df, n))

if __name__ == "__main__":
    main()
