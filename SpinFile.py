# A4 Word Spinner Solo work by Ruixiang Li U1388321 URL：https://github.com/RuixaingLi/my-A4


from Spinner import Spinner
import string

def main():
    def remove_punctuation(text):
        translator = str.maketrans('', '', string.punctuation)
        return text.translate(translator)


    with open('essay.txt') as file:
        Original_essay = file.read()

    essay = remove_punctuation(Original_essay.lower())
    for count in range(3):
        mytest = Spinner()

        mytest = mytest.look_for_keyword(essay)

        print("Original"+str(count+1)+": " + Original_essay, end="")  # if it is a long sentence it will look much
        # better with end=""
        print("Replaced"+str(count+1)+": " + mytest)
        print()

if __name__ == "__main__":
    main()