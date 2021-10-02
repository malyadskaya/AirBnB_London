# We need to save union and cleaned data somewhere,
# in our exact case it won't be new table in some db as usual but just another csv file

class clean_data_store:
    def __init__(self, df, path_to_save, file_name):
        self.df = df
        self.path_to_save = path_to_save
        self.file_name = file_name

    def saving_to_csv(self, df, path_to_save, file_name):
        df.to_csv(path_to_save + '/' + file_name + '.csv',
                  index=False,
                  encoding='utf-8',
                  sep='\t',
                  date_format='%Y-%m-%d')
#         was using this wired separator to not mix the string columns up course we work with csvs here..
