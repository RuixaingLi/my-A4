# A4 Word Spinner Solo work by Ruixiang Li U1388321 URL：https://github.com/RuixaingLi/my-A4
import random


class Spinner:
    def __init__(self):
        self.replace_dic = self.read_synonym()

    def read_synonym(self):
        synonym_dic = {}
        with open("synonyms-simplified.txt") as file:
            for things in file:
                things_without_space = things.strip()
                key = things_without_space.split(':')[0]
                value = things_without_space.split(':')[1]
                value_list = value.split(",")
                synonym_dic[key] = value_list
        return synonym_dic

    def look_for_keyword(self, essay_txt):
        words = essay_txt.split()
        replaced_list = []
        for word in words:
            randint = random.randint(0, 100)
            if randint > 50:
                if word in self.replace_dic:
                    synonym_list = self.replace_dic[word]
                    replacement = random.choice(synonym_list)
                    replaced_list.append(replacement)
                else:
                    replaced_list.append(word)
            else:
                replaced_list.append(word)
        my_replaced_string = ' '.join(replaced_list)
        return my_replaced_string
