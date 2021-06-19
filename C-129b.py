import csv
dataset1=[]
dataset2=[]
with open("dataset_1.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataset1.append(row)
Headers1=dataset1[0]
PlanetData1=dataset1[1:]
with open("dataset2sorted.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        dataset2.append(row)
Headers2=dataset2[0]
PlanetData2=dataset2[1:]
Header=Headers1+Headers2
PlanetData=[]
for index,datarow in enumerate(PlanetData1):
    PlanetData.append(PlanetData1[index]+PlanetData2[index])
with open("final.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(Header)
    csvwriter.writerows(PlanetData)
    