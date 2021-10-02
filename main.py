from data_collecting import data_collecting_to_df
from data_cleaning import data_cleaning_to_df, find_outliers_sep
from data_saving import clean_data_store
from navigation import row_data_path, cleaned_data_path, null_values_perc, outliers_to_remove, dt_col, num_col, str_col
import pandas as pd
import numpy as np

if __name__ == '__main__':
    obj0 = data_collecting_to_df(row_data_path)
    df_collected = obj0.df_from_files()

    obj = data_cleaning_to_df(df_collected, null_values_perc, outliers_to_remove, dt_col, num_col)
    df_no_nulls = obj.remove_columns_with_lots_of_nulls(df_collected, null_values_perc)

    obj = data_cleaning_to_df(df_no_nulls, null_values_perc, outliers_to_remove, dt_col, num_col)
    df_no_dups = obj.remove_dups(df_no_nulls)

    obj = data_cleaning_to_df(df_no_dups, null_values_perc, outliers_to_remove, dt_col, num_col)
    df_dtypes = obj.to_date_type(df_no_dups, dt_col, num_col, str_col)

    obj = data_cleaning_to_df(df_dtypes, null_values_perc, outliers_to_remove, dt_col, num_col)
    df_fill_nulls = obj.fill_nulls(df_dtypes, dt_col, num_col)

    obj2 = find_outliers_sep(df_fill_nulls, outliers_to_remove)
    df_outliers = obj2.find_outliers(df_fill_nulls, outliers_to_remove)

# we won't remove outliers in this case, just will save them to separate file

    obj_s1 = clean_data_store(df_fill_nulls, cleaned_data_path, 'union_data')
    obj_s1.saving_to_csv(df_fill_nulls, cleaned_data_path, file_name='union_data')

    obj_s2 = clean_data_store(df_outliers, cleaned_data_path, 'outliers')
    obj_s2.saving_to_csv(df_outliers, cleaned_data_path, file_name='outliers')
