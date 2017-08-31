import pandas as pd
from sklearn.neighbors import NearestNeighbors


def based_on_knn(product_featured, product, n_neighbors):
    """
    KNN
    """
    X = product_featured.values

    model = NearestNeighbors(n_neighbors=n_neighbors)
    trained_model = model.fit(X)

    return trained_model.kneighbors(product)


def main():

    n_neighbors = 5

    product_featured = pd.read_csv('product_features.csv')
    product = pd.read_csv('product.csv')

    result = based_on_knn(product_featured, product, n_neighbors)

    print('Product to label')
    print(product)
    print('Product closest by features are {}'.format(list(result[1][0])))
    print(product_featured.iloc[list(result[1][0])])


if __name__ == "__main__":
    main()
