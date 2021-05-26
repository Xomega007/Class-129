import csv

dataset_1 = []
dataset_2 = []

with open(r"C:\Users\vedan\Desktop\Pre-Processing\data1.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open(r"C:\Users\vedan\Desktop\Pre-Processing\data2.csv","r") as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

header1 = dataset_1[0]
planet_data1 = dataset_1[1: ]

header2 = dataset_2[0]
planet_data2 = dataset_2[1: ]

headers = header1 + header2
planet_data = []

for index,data_row in enumerate(planet_data1):
    planet_data.append(planet_data1[index]+planet_data2[index])

with open("merge_data.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)
    csvwriter.writerows(planet_data)