class Getdata():

    import pandas as pd

    def load_data(url):
        df = pd.read_csv(url)
    return df

    def describe(df):
    return df.describe()


#to check if it has null values
    def have nulls(df):
        nulls = df.isnull().sum()
    if nulls == 0:
        print('You have no null values')
    elif nulls >= 0:
        print('You have nulls =', nulls)


class Cleaning():

    import numpy as np
    def __init__(self, df):
        self.df = df

    def remove_nulls(self, value={np.nan, '?', ' ', new = 0):
        #replaces nan's with 0s
        #next, I want to write where we can replace any nan, blank, or ?
        #value with 0
        self.df = self.df.replace(value, new)

#    def impute_values(self):
#would come back to this.

#helper function
def value_counts10(df):
    counts = pd.value_counts.head(10)
    return counts

#Splitting data using three-way test Splitting

def threewaysplit(df):
    from sklearn.model_selection import train_test_split
    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size = 0.2, random_state, stratify = y
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train, y_train, test_size = 0.3, random_state = 42, stratify = y_train
    )

    return X_train, X_test, y_train, y_test
