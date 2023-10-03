def read_synonym():
    synonym_dic = {}
    with open("test-synonyms.txt") as file:
        for things in file:
            key = things.split(':')[0]
            value = things.split(':')[1]
            synonym_dic[key] = value
    return synonym_dic
test_myfunction = read_synonym()
print(test_myfunction)

#class Spineer:
    #def __init__(self):
