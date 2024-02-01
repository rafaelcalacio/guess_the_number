import random

#gera numero aleatorio entre 1 e 100
def gera():
    return random.randint(1,20)

def game():
    numero = gera()
    print("Número aleatório gerado com sucesso!!!")
    palpite = 0
    tentativa = 0
    while palpite != numero:
        tentativa += 1
        print(f"Tentativa: {tentativa}\n")
        palpite = int(input("Digite um núme entre 1 e 20\n"))
        if palpite > numero:
            print("O número é menor!!!")
        elif palpite < numero:
            print("O numero é maior!!!")
        else:
            print(f"Você acertou, o número sorteado é {numero} \nVocê conseguiu em {tentativa} tentativas!!!")

game()


