import pandas as pd
import numpy as np
from sklearn.decomposition import TruncatedSVD


def based_on_svd(ratings_df, products_df, name, corr_value):
    """
    1000 people with 50 products. We got 10000 recommendations so in average each person recommend 10 product
    """
    # Utility  1000x50  1000 people x 50 product
    ratings_pivot = pd.pivot_table(data=ratings_df, values='rating', index='userID', columns='productID', fill_value=0)

    # Transposing
    X = ratings_pivot.T  # 50x1000  50 product x 1000 people

    # Truncate to build a matrix with 'features' (12 but you can change) so M = L x U
    SVD = TruncatedSVD(n_components=12, random_state=17)
    decomposed_matrix = SVD.fit_transform(X)  # 50x12  50 products x 12 features

    # correlation matrix
    corr_mat = np.corrcoef(decomposed_matrix)  # we got 50x50, diagonal [[1, 0.2], [0.2, 1]]

    # get the product id input by user
    index_column = products_df[products_df['productName'] == name].index[0]

    # get the correlation values of the product respect to the rest, corr of the product with itself = 1
    product_corr_values = corr_mat[index_column]

    # mask values of dataframe with values of corr higher than....
    return products_df[product_corr_values >= corr_value]


def main():
    # client requirements, highly correlated product with name:
    name = 'CNIwdVaBLH'
    corr_value = 0.7

    # model source
    ratings_df = pd.read_csv('product_ratings.csv')
    products_df = pd.read_csv('product_list.csv')

    # feedback
    result = based_on_svd(ratings_df, products_df, name, corr_value)
    print(result)

if __name__ == "__main__":
    main()
