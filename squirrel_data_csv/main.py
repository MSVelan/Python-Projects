import pandas
data = pandas.read_csv('./squirrel_data_csv/2018_Squirrel_Census.csv')
furcolumn = data["Primary Fur Color"]
d = {}
for i in furcolumn:
    if(i not in d.keys()):
        d[i] = 1
    else:
        d[i]+=1

csvData = {"furcolumn":d.keys(),"count":d.values()}

dataf = pandas.DataFrame(csvData)
dataf.to_csv("./squirrel_data_csv/squirrel_fur_count_generatedFromPython.csv")
