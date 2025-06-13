 
 
 
 #read the csv without Pandas
import csv
 
with open("wheater_data.csv") as data_file:
    data=csv.reader(data_file)
    temperatures =[]
    for row in data:
        if row[1] !="temp":
            temperatures.apped(int(row[1]))
    print(temperatures)
    
    #read csv with Pandas
        
import pandas
pandas.read_csv("wheater_data.csv")
print(data)
print(data["temp"])

data_dict=data.to_dict()
print(data_dict)

temp_list=data["temp"].to_list()
print(len(temp_list))

print(data["temp"].mean())   
print(data["temp"].max())

# Get data in columns
print(data["condition"])
print(data.condition)
      
# Get data in rows
print(data[data.day == "Monday"])
data.temp==data.temp.max()
    