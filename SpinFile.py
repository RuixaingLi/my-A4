from main import Spinner
import string


def remove_punctuation(text):
    translator = str.maketrans('', '', string.punctuation)
    return text.translate(translator)


with open('essay.txt') as file:
    Original_essay = file.read()

essay = remove_punctuation(Original_essay.lower())
for count in range(3):
    mytest = Spinner()

    mytest = mytest.look_for_keyword(essay)
    print("Original" + str(count + 1) + ": " + Original_essay, end="")  # looks much better with it
    print("Replaced" + str(count + 1) + ": " + mytest)
    print()
