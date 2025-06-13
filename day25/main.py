 
 
 
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
        
     