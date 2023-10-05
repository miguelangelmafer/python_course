import pandas

data = pandas.read_csv("weather_data.csv")

print(data["temp"])

# convert it to a dictionary
data_dict = data.to_dict()
print(data_dict)

# convert it to a list
temp_list = data["temp"].to_list()
print(temp_list)

# Average temp
print(data["temp"].mean())
# Max temp
print(data["temp"].max())

print(data.condition)

# Get data in a row
print(data[data.day == "Monday"])
print(data[data.temp == data["temp"].max()])

monday = data[data.day == "Monday"]

# Monday temp in Fahrenheit (0 °C × 9 / 5) + 32
print((monday.temp[0] * 9) / 5 + 32)

# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 83]
}

data2 = pandas.DataFrame(data_dict)

print(data2)
data2.to_csv("output.csv")
