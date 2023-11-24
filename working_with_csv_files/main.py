# with open("./working_with_csv_files/Sample_weatherdata.csv") as f:
#     l = f.readlines()

# print(l)

# import csv

# with open("./working_with_csv_files/Sample_weatherdata.csv") as f:
#     data = csv.reader(f)
#     temperatures = []
#     for row in data:
#         if(row[1]!='temp'):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

data = pandas.read_csv("./working_with_csv_files/Sample_weatherdata.csv")
# print(data['temp'])

d = data.to_dict()
# print(d)

# tempList = data['temp'].to_list()
# print(tempList)
# avg_temp = sum(tempList)/len(tempList)
# print(avg_temp)


# avg = data['temp'].mean()
# print(avg)

# print(data['temp'].sum()/data['temp'].size)

# print(data['temp'].max())

# print(data[data['temp']==data['temp'].max()])
# print(type(data['temp'].max()))

monday = data[data.day == 'Monday']
# print(monday)

def converttofahrenheit(x):
    return x*9/5+32
# print(monday.temp.apply(converttofahrenheit))

data_dict = {"students":["MSV",'Mithil','Lives','Aradhya'],"score":[100,90,92,91]}
newdata = pandas.DataFrame(data_dict)
newdata.to_csv("./working_with_csv_files/csvFileUsingPandas.csv")