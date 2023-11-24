# import random
# names = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']
# student_scores = {i:random.randint(1,100) for i in names}
# print(student_scores)
# passed_students = {k:v for k,v in student_scores.items() if v>=60}
# print(passed_students)


# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

# result = {word:len(word) for word in sentence.split()}

# print(result)

# weather_c = {
#     "Monday": 12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24
# }

# weather_f = {k:9*v/5+32 for (k,v) in weather_c.items()}
# print(weather_f)

import pandas,random

snames = ['Alex','Beth','Caroline','Dave','Eleanor','Freddie']

s_dict = {k:random.randint(1,100) for k in snames}

student_dict = {"Name":s_dict.keys(),"Marks":s_dict.values()}
sdf = pandas.DataFrame(student_dict)
print(sdf)

for index,row in sdf.iterrows():
    print(row.Name," ",row.Marks)