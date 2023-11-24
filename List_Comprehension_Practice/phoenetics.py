import pandas

phoeneticsdf = pandas.read_csv("./List_Comprehension_Practice/NATO_Phoenetics.csv")

data_dict = {row.letter:row.code for (index,row) in phoeneticsdf.iterrows()}
word = input("Enter a word:")
while True:
    try:
        l = [data_dict[i.upper()] for i in word]
    except KeyError:
        print("Sorry, enter only letters")
    else:
        break
print(l)