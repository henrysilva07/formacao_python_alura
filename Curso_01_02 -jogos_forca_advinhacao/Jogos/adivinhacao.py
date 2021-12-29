import random

def jogar():
    
    print("******************************************")
    print("\nBem-Vindo ao jogo de advinhação\n")
    print("******************************************")

    #variável para armazenar o números de tentativas do usuário
    total_de_tentativas = 0 
    #retorna o número secreto: o método randrange() retorna um valor aleatório do intervalo
    numero_secreto = random.randrange(1,101)
    pontos = 1000


    print("Qual o nível da dificuldade?")
    print("(1) - Fácil (2) - Médio (3) - Difícil")
    nivel = int(input("Defina o nível: "))

    if (nivel== 1):
        total_de_tentativas = 20
    elif (nivel == 2 ):
        total_de_tentativas = 101
    else:
        total_de_tentativas = 5



    for rodada in range(1, total_de_tentativas + 1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if (chute < 1 ) or (chute > 100):
            print("Você deve digitar um número ente 1 e 100\n")
            
            continue

        acertou = numero_secreto == chute
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Parabens! Você acertou e fez {} pontos".format(pontos))
            input("Aperte enter para continuar...")
            break
        else:
            if (maior):
                print("Você errou! O seu chute foi maior que o número secreto.")
            elif (menor):
                print("Você errou! O seu chute foi menor que o número secreto.")

            pontos_perdidos = abs( numero_secreto - chute)
            pontos = pontos - pontos_perdidos
            

    print("Fim do jogo")


if (__name__ == "__main__"):
    jogar()