import random

hanged = {
    1 : "       (x_x)\n",
    2 : "       (x_x)    \n" +
        "     +==| |==+  \n",
    3 : "       (x_x)    \n" +
        "     +==| |==+  \n" +
        "        |_|     \n",
    4 : "       (x_x)    \n" +
        "     +==| |==+  \n" +
        "        |_|     \n" +
        "        / \\     \n",
    5 : "       (x_x)    \n" +
        "     +==| |==+  \n" +
        "        |_|     \n" +
        "        / \\     \n" +
        "      _<   >_    \n",
    6 : "  ___         ___\n" +
        "  \\  \\_(x_x)_/  /\n" +
        "   \\ +==| |==+ / \n" +
        "    ^^^^|_|^^^^  \n" +
        "        / \\      \n" +
        "      _<   >_    \n",
    7 : "\n"
        ":^/  GAMER OVER  :^(\n"
        "  ___   ===   ___\n" +
        "  \\  \\_(x_x)_/  /\n" +
        "   \\ +==| |==+ / \n" +
        "    ^^^^|_|^^^^  \n" +
        "        / \\      \n" +
        "      _<   >_    \n",
}

__attempts__ = 7

def hangman_game():

    hit = {}
    bad_hits = []
    secret_words_list = load_words()
    secret_word = draw_word(secret_words_list)

    # print(secret_words_list)
    # print(secret_word)

    display_header()

    while(was_guessed_word(secret_word, hit) and was_hanged(bad_hits)):

        show_shot(hit, secret_word, bad_hits)
        shot = input("  ?? Your Shot: ")
        hit[shot] = True

        if(has_letter(shot, secret_word)):
            print("You guessed right! Your shot is in the word.")
        else:
            bad_hits.append(shot)
            print("You guessed wrong! Your shot is not in the word.")

    print("\nEnd Game!")
    print("The secret word was: {}".format(secret_word))

    if(was_guessed_word(secret_word, hit)):
        print("TRY AGAIN!")
    else:
        print("CONGRATULATIONS! YOU DID IT, YOU DISCOVERED THE SECRET WORD!\n")
        answer = input("Would you like to add a new word to the word bank? [Y/N]: ")

        if(answer == "Y"):
            add_word()



def display_header():
    print("+++++++++++++++++++++++++++++")
    print("+ Welcome to Hangman Game! +")
    print("+++++++++++++++++++++++++++++")

    print("\nHANGMAN GAME")

def load_words():
    try:
        # with open('words.txt', 'r') as f:
        #     word_list = [line.rstrip() for line in f]

        file_buffer = open('words.txt', 'r', encoding="utf-8")
        word_list = [line.strip() for line in file_buffer]
        file_buffer.close()

        return word_list

    except:
        print("@ WARNING:")
        print("\tCannot open the file!")
        print("\tThe application can be run. And it will close!")
        exit(0)

def draw_word(words_list):
    return words_list[random.randrange(len(words_list))]

def was_guessed_word(secret_word, hit):
    for letter in secret_word:
        if(letter not in hit.keys()):
            return True
    return False

def was_hanged(bad_hits):
    if(len(bad_hits) == 0):
        return True

    print(hanged[len(bad_hits)])
    return len(bad_hits) < 7

def show_shot(hit, secret_word, bad_hits):

    print(":^( chutes errados: ", end='')

    for letter in bad_hits:
        print(letter, " ", sep='', end='')
    print('', sep='')

    for letter in secret_word:
        if(letter in hit.keys()):
            print(letter, " ", sep='', end='')
        else:
            print("_ ", sep='', end='')

def has_letter(shot, secret_word):
    for letter in secret_word:
        if(letter == shot):
            return True
    return False

def add_word():
    new_word = input("Insert new word in capital letters: ")
    words_list = load_words()
    words_list.append(new_word)
    save_file(words_list)

def save_file(words_list):
    try:
        file_buffer = open('words.txt', 'w', encoding="utf-8")

        last_word = words_list.pop()

        for line in words_list:
            file_buffer.write(line)
            file_buffer.write('\n')

        file_buffer.write(last_word)

        file_buffer.close()

    except:
        print("@ WARNING:")
        print("\tCannot open the file!")
        print("\tThe application can be run. And it will close!")
        exit(0)

# If this file is "main" than run hangman game
if (__name__ == "__main__"):
    hangman_game()