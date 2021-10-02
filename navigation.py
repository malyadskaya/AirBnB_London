# path where our file collected
row_data_path = '/Users/Anastasiyam/PycharmProjects/AirBnB_London/row_data'
# path to save clean data
cleaned_data_path = '/Users/Anastasiyam/PycharmProjects/AirBnB_London/clean_data'
# columns need to be converted to date
dt_col = ['last_review']
# columns need to be int
num_col = ['id', 'host_id', 'latitude', 'longitude', 'price', 'minimum_nights', 'number_of_reviews', 'reviews_per_month', 'calculated_host_listings_count', 'availability_365']
# columns need to be str
str_col = ['name', 'host_name', 'neighbourhood_group', 'neighbourhood', 'room_type']
# when the column has 80% or more null values we'll remove it
null_values_perc: float = 0.8
# numeric columns where we can find outliers
outliers_to_remove: list = ['price', 'number_of_reviews', 'calculated_host_listings_count']