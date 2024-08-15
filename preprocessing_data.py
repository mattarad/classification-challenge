import pandas as pd

def get_X_y(df, target):
    """
        Takes in a pandas data frame and the string name of the target column
        returns two data frames
        1) drops the target column and returns the rest of the data frame
        2) returns a dataframe of the target column
    """
    return df.drop(target, axis=1), df[target]