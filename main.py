# class Spinner:
#     def __init__(self):
def read_synonym():
    synonym_dic = {}
    with open("test-synonyms.txt") as file:
        for things in file:
            things_without_space = things.strip()
            key = things_without_space.split(':')[0]
            value = things_without_space.split(':')[1]
            value_list = value.split(",")
            synonym_dic[key] = value_list
    return synonym_dic
