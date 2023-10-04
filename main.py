
import string
class Spinner:
    def __init__(self):
        self.replace_dic = self.read_synonym()

    def read_synonym(self):
        synonym_dic = {}
        with open("test-synonyms.txt") as file:
            for things in file:
                things_withouspace = things.strip()
                key = things_withouspace.split(':')[0]
                value = things_withouspace.split(':')[1]
                value_list = value.split(",")
                synonym_dic[key] = value_list
        return synonym_dic
    def look_for_keyword(self):
        replaced_string = []
        for word in self.replace_dic:
            if word in self.replace_dic:
                synonym_list =self.replace_dic[word]
                replacement = synonym_list
                replaced_string.append(replacement)
            else:
                replaced_string.append(word)
        return replaced_string