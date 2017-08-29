import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report


def based_on_logreg(x, report=True):

    product_featured = pd.read_csv('product_featured.csv')

    X = product_featured.ix[:, :-1].values  # all columns but last as inputs features for model
    y = product_featured.ix[:, -1].values  # last column to predict. input labels

    x = x.values  # what we want to classified

    model = LogisticRegression()
    model_trained = model.fit(X, y)
    y_pred = model_trained.predict(x)

    if report:
        Y_pred = model_trained.predict(X)  # we predict Y for X(real), and then we compare with y(real)
        print(classification_report(y, Y_pred))

    return y_pred


def main():

    new_client = pd.read_csv('product.csv')

    y_pred = based_on_logreg(new_client, report=True)
    print("Is this person valid for this Product? {}".format("Yes" if y_pred == 1 else "No"))

if __name__ == '__main__':
    main()
