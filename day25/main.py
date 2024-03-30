import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# grabbing Primary Fur Color and counting the length for each color
gray = len(data[data["Primary Fur Color"] == "Gray"])
black = len(data[data["Primary Fur Color"] == "Black"])
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])


squirrel_count = {
    "Fur Color": ["gray", "black", "cinnamon"],
    "Count": [gray, black, cinnamon]
}

squirrel_count_df = pandas.DataFrame(squirrel_count)
squirrel_count_df.to_csv("squirrel_count.csv")

