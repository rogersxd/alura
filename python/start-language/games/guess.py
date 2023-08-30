import random

def start():
    print("************************************")
    print("* Bem vindo ao jogo de Adivinhação *")
    print("************************************")

    initial_score = 100
    score = initial_score
    total_tries = 3
    secret_number = random.randrange(1, 11)

    print("Escolha um nível de dificuldade:")
    print("(1) Fácil | (2) Médio | (3) Difícil")

    level = int(input("Digite o nível que deseja:"))

    if level == 1:
        total_tries = 10
    elif level == 2:
        total_tries = 5

    for game in range(1, total_tries + 1):
        print("Tentativa:", game, " de ", total_tries)

        kick = input("Digite um número entre 1 e 10: ")
        kick = int(kick)

        print("Você digitou o número: ", kick)

        correct = kick != secret_number
        grater = kick > secret_number
        less = kick < secret_number

        if kick < 0 or kick > 10:
            print("Você deve digitar um número entre 1 e 10.")
            continue

        if correct:
            if grater:
                print("Você errou! Seu chute foi maior que o número secreto.")
            elif less:
                print("Você errou! Seu chute foi menor que o número secreto.")

            score -= (initial_score / total_tries)
        else:
            print("Você acertou!")
            break

    if score < 0:
        score = 0

    print("Pontuação:", score)
    print("Fim do jogo")

if __name__ == "__main__":
    start()