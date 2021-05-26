import csv

data = []

with open(r"C:\Users\vedan\Desktop\Pre-Processing\data1.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        data.append(row)

headers = data[0]
planet_data = data[1: ]

#Changind to lowercase
for data_point in planet_data:
    data_point[2] = data_point[2].lower()

#Making it alphabetical order
planet_data.sort(key = lambda planet_data : planet_data[2])

#Creating new file
with open("data_2_sort.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)