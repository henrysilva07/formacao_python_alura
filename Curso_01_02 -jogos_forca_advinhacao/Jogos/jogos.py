
import forca
import adivinhacao

print("*********************************")
print("******* Escolha o seu jogo! *******")
print("*********************************")

print("(1) Forca (2) Adivinhação")

opcao = int(input("Defina um jogo: "))

if (opcao == 1):
    forca.jogar()

elif (opcao == 2):
    adivinhacao.jogar()