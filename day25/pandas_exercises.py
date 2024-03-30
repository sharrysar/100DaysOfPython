import pandas

# dataframe
data = pandas.read_csv("weather_data.csv")

# series
temp_list = data["temp"].to_list()

# find avg from series
temp_avg = data['temp'].mean()

# find max
temp_max = data['temp'].max()

# get data in row
max_row = data[data.temp == temp_max]

# get monday's temp value only
monday_c = data[data.day == 'Monday'].temp
monday_f = (monday_c * 9/5) + 32

# create a dataframe
new_dict = {
    "names": ["blossom", "bubbles", "buttercup"],
    "colors": ["red", "blue", "green"]
}

new_data = pandas.DataFrame(new_dict)

# save new_data to csv file
new_data.to_csv("new_data.csv")

