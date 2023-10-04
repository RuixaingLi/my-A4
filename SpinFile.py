from main import Spinner
import string

def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)

with open('essay.txt') as file:
    essay= file.read()

essay = remove_punctuation(essay.lower())

mytest = Spinner()

mytest = mytest.look_for_keyword(essay)

print(mytest)