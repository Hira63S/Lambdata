class Getdata():
    import pandas as pd

    def load_data(url):
        df = pd.read_csv(url)

    return df

    def describe():

    return pd.describe()

    def

pass

class cleaning:

    import numpy as np
    def __init__(self, df):
        self.df = df


    def remove_nulls(self, value=np.nan, new = 0):
        #replaces nan's with 0s
        #next, I want to write where we can replace any nan, blank, or ?
        #value with 0
        self.df = self.df.replace(value, new)

#    def impute_values(self):
#would come back to this.

#helper function

def value_counts10():
    counts = pd.value_counts.head(10)

    return counts
