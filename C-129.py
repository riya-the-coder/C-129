import csv
data=[]
with open("dataset_2.csv","r")as f:
    csvReader=csv.reader(f)
    for row in csvReader:
        data.append(row)
Headers=data[0]
PlanetData=data[1:]
for dataPoint in PlanetData:
    dataPoint[2]=dataPoint[2].lower()
PlanetData.sort(key=lambda PlanetData:PlanetData[2])
with open("dataset2sorted.csv","a+")as f:
    csvwriter=csv.writer(f)
    csvwriter.writerow(Headers)
    csvwriter.writerows(PlanetData)
    