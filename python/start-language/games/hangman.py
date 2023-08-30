import random

def start():
    print("************************************")
    print("* Bem vindo ao jogo da Forca *")
    print("************************************")

    words = []

    file = open("words.txt", "r")

    for row in file:
        row = row.strip()
        words.append(row.upper())

    file.close()

    random_position_word = random.randrange(0, len(words))
    secret_word = words[random_position_word]
    correct_letters = ["_" for letter in secret_word]

    hanged = False
    win = False
    tries = 3

    print(correct_letters)

    while not hanged and not win:

        kick = input("Digite uma letra:")
        kick = kick.upper()
        kick = kick.strip()

        index = 0
        if kick in secret_word:

            for letter in secret_word:
                if kick == letter:
                    correct_letters[index] = letter
                index += 1
        else:
            tries -= 1

        hanged = tries == 0
        win = "_" not in correct_letters

        print(correct_letters)

    if win:
        print_won_message()
    else:
        print_lose_message(secret_word)

    print("Fim do jogo")

def print_won_message():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")

def print_lose_message(secret_word):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secret_word))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print(" /                   \     ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXXX     XXXX   |     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")

if __name__ == "__main__":
    start()