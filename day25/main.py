import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirrel_dict = {
    "Fur Color" : ["grey" , "black" , "red"],
    "count": [0 , 0 , 0]
}


red = data[data["Primary Fur Color"] == "Cinnamon"]
gray = data[data["Primary Fur Color"] == "Gray"]
black = data[data["Primary Fur Color"] == "Black"]



squirrel_dict["count"][0] = len(gray)
squirrel_dict["count"][1] = len(black)
squirrel_dict["count"][2] = len(red)

ok = pandas.DataFrame(squirrel_dict)
ok.to_csv("squirrel_data.csv")