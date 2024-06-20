# with open("./weather_data.csv") as f:
#     data = f.readlines()
# print(data)
# import csv
# with open("weather_data.csv") as f:
#     data = csv.reader(f)
#     temperature = []
#     data_list = []
#     for row in data:
#         data_list.append(row)
#     for row in data_list[1:]:
#         temperature.append(int(row[1]))
#     print(temperature)

import pandas as pd
# data = pd.read_csv("weather_data.csv")
#print(data["temp"].max())
#print(data[data.temp == data.temp.max()])
# print(data[data.day == "Monday"].temp[0] * 9 / 5 + 33)

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240210.csv")
gdata = data.groupby(["Primary Fur Color"], as_index=False)["Unique Squirrel ID"].count()
gdata.to_csv("result.csv")