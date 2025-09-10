from my_utils import get_column

country = 'United States of America'
country_column = 0  # countries are in column 0, not 1
fires_column = 4
file_name = 'Agrofood_co2_emission.csv'

# get the fire data for this country
fires = get_column(file_name, country_column, country, result_column=fires_column)
print(fires)
