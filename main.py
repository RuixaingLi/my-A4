import random


class Spinner:
    def __init__(self):
        self.replace_dic = self.read_synonym()

    def read_synonym(self):
        synonym_dic = {}
        with open("test-synonyms.txt") as file:
            for things in file:
                things_withoutspace = things.strip()
                key = things_withoutspace.split(':')[0]
                value = things_withoutspace.split(':')[1]
                value_list = value.split(",")
                synonym_dic[key] = value_list
        return synonym_dic

    def random_replace(self):
        self.randint = random.randint(0, 100)
        if self.randint > 50:
            return True
        else:
            return False

    def look_for_keyword(self, essay_txt):
        words = essay_txt.split()
        replaced_list = []
        for word in words:
            if word in self.replace_dic:
                synonym_list = self.replace_dic[word]
                random_replace(replacement) = random.choice(synonym_list)
                replaced_list.append(replacement)
            else:
                replaced_list.append(word)
        my_replaced_string = ' '.join(replaced_list)
        return my_replaced_string
