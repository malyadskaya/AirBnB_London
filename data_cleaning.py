import pandas as pd
from scipy import stats
import numpy as np


# After we have df we also could to save row data to some separate cluster to have all the raw data,
# also in case smth will happen with our flow and we'll need to rerun on some time period.
# Before loading it to some table in db for analyzing we'll clean the data a bit.

class data_cleaning_to_df:
    def __init__(self, df, null_values_perc, outliers_to_remove, dt_col, num_col):
        self.df = df
        self.null_values_perc = null_values_perc
        self.outliers_to_remove = outliers_to_remove
        self.dt_col = dt_col
        self.num_col = num_col

    # remove columns with large amount of null values, also optional
    def remove_columns_with_lots_of_nulls(self, df, null_values_perc):
        return df[df.columns[df.isnull().mean() < null_values_perc]]

    def remove_dups(self, df):
        return df.drop_duplicates()

    # we'll convert last_review column to date, numeric columns to nums and others will go as str,
    # here we don't have other datatypes
    def to_date_type(self, df, dt_col, num_col, str_col):
        for col in df.columns:
            if col in dt_col:
                df[col] = pd.to_datetime(df[col])
            elif col in num_col:
                df[col] = pd.to_numeric(df[col])
            elif col in str_col:
                df[col] = df[col].astype(str)
        return df

    # will fill nans with some default values
    def fill_nulls(self, df, dt_col, num_col):
        for nc in df.columns:
            if nc in num_col:
                df[nc] = df[nc].replace('nan', 0)
            elif nc in dt_col:
                df[nc] = df[nc].fillna(pd.to_datetime(str('1900-01-01').split()[0]))
            else:
                df[nc] = df[nc].replace('nan', 'No_info')
        return df

    # # In case we want more clear data for analyzing will remove outliers for numeric values, but will leave it for now
    # def remove_outliers(self, df, outliers_to_remove):
    #     return df[(np.abs(stats.zscore(df[outliers_to_remove])) < 3).all(axis=1)]


# We'll want to analyze all the outliers separately.
class find_outliers_sep:
    def __init__(self, df, outliers_to_remove):
        self.df = df
        self.outliers_to_remove = outliers_to_remove

    def find_outliers(self, df, outliers_to_remove):
        return df[(np.abs(stats.zscore(df[outliers_to_remove])) >= 3).all(axis=1)]
