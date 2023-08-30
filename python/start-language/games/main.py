import guess
import hangman

def select_game():
    print("************************************")
    print("* Escolha um jogo *")
    print("************************************")

    print("(1) Adivinhação | (2) Forca")

    selected_game = int(input("Qual você quer jogar?"))

    if selected_game == 1:
        guess.start()
    else:
        hangman.start()

if __name__ == "__main__":
    select_game()