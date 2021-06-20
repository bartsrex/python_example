"""bla bla"""

from GUI import Window



def main():
    """ba bla bla"""

    win = Window()
    Window.initWindow(win)


if __name__ == "__main__":
    main()

def count_words(word):
    list_all = word.split()
    word_list = list(filter(lambda i: len(i) >= 3, list_all))
    number_of_words = len(word_list)
    return number_of_words
