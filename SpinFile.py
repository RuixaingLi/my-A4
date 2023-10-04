# A4 Word Spinner Solo work by Ruixiang Li U1388321 URL：https://github.com/RuixaingLi/my-A4


from Spinner import Spinner
import string


def main():
    def remove_punctuation(text):
        remove = str.maketrans('', '', string.punctuation)
        return text.translate(remove)

    with open('essay.txt') as file:
        original_essay = file.read()

    essay = remove_punctuation(original_essay.lower())
    print("Original1: " + original_essay)  # if it is a sentences without punctuation it will look much better with
    # end=""
    print()
    for count in range(3):
        mytest = Spinner()

        mytest = mytest.look_for_keyword(essay)

        print("Option" + str(count + 1) + ": " + mytest)
        print()  # make sentences look better


if __name__ == "__main__":
    main()
