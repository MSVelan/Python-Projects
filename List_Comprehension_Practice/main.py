with open('./List_Comprehension_Practice/file1.txt') as f1:
    l = f1.readlines()
    l1 = [int(i.rstrip('\n')) for i in l]

with open('./List_Comprehension_Practice/file2.txt') as f2:
    l = f2.readlines()
    l2 = [int(i.rstrip('\n')) for i in l]

l3 = [i for i in l1 if(i in l2)]
print(l3)