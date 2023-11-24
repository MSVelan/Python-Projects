with open('./Input/names.txt') as f:
    l = f.readlines()
    f1 = open('./Input/starting_letter.docx')
    contents = f1.read()
    for i in l:
        name = i.rstrip('\n')
        f2 = open(f'./Output/{name}.docx','w')
        i = contents.find('[name]')
        if(i!=-1):
            f2.write(contents[:i])
            f2.write(name)
            f2.write(contents[i+6:])
        f2.close()
    f1.close()