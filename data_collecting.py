import glob
import pandas as pd
from navigation import row_data_path

# Let's say all of a sudden we're getting csv files in the same format
# (most probably for such kind of data we'll have streaming and connecting will be to some batches,
# in our imaginary case it is one-year-batches)
# In some cases more comfortable to work with json formats but for our current case I prefer dataframe.
# So I'm extracting all those csvs together to dataframe with adding year column (no date and inserted_time)
# Since we don't have much data here I upload it one time and in the end I see it as partitioned by year table.
# For more usual data flow we'll be just adding new data (partition),
# TODO: adding new data (partition)
# and maybe rerun some previous period in case of some changes happen (very popular for payments processes, retention),
# it will happen either once in a period or by some trigger.


class data_collecting_to_df:
    def __init__(self, path: str):
        self.path = path

    def df_from_files(self):
        all_files = glob.glob(self.path + "/*.csv")
        listings = []
        for filename in all_files:
            yr = filename[-8:-4]
            df = pd.read_csv(filename, index_col=None, header=0)
            df['yr'] = yr
            listings.append(df)
        df_listings = pd.concat(listings, axis=0, ignore_index=True)
        return df_listings


# df = data_collecting_to_df(row_data_path)
# print(df.df_from_files().head())
