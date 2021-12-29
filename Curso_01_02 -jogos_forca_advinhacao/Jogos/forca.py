import random


def imprimir_abertura():

    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")


def carregar_palavras(nome_arquivo = "palavras.txt"):

    palavras = []
    with open(nome_arquivo, 'r') as arquivo:
        
        for linha in arquivo:
            linha = linha.strip()
            palavras.append(linha)

    numero = random.randrange(0, len(palavras))

    palavra = palavras[numero].upper()

    return palavra

def inicializar_letras_acertas( palavra):

    letras = [ "_"  for i in palavra]

    return letras

def pedir_chute():

    chute = input("Qual letra?\n")
    chute = chute.strip().upper()

    return chute

def marcar_chute_correto(chute, palavra, letras):
    index = 0
    for letra in palavra:
        if (chute == letra):
            letras[index] = letra
        index += 1


def imprime_mensagem_vencedor():
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

def imprime_mensagem_perdedor(palavra_secreta):
    print("Poxa, você foi enforcado!")
    print("A palavra era {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
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


def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")
        print(" |            ")
        print("_|___         ")
        print()


def jogar():

    imprimir_abertura()
    palavra_secreta = carregar_palavras()
   
    letras_acertadas = inicializar_letras_acertas(palavra_secreta)

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while (not acertou and not enforcou):

        chute = pedir_chute()
        if (chute in palavra_secreta):
            marcar_chute_correto(chute, palavra_secreta , letras_acertadas)
            
        else:
            erros += 1
            desenha_forca(erros)
            

        if (erros == 7):
            break
        if( "_" not in letras_acertadas ):
            print(letras_acertadas)
            break

        print(letras_acertadas)

    print("Fim do jogo")

    if ("_" not in letras_acertadas):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)


if (__name__ == "__main__"):
    jogar()