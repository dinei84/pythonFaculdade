import random

print("Digite um numero de 0 a 5")

numero = int(input("Que numero pensei?: "))

lista = [1,2,3,4,5]

sorteio = random.choice(lista)

if sorteio == numero:
    print("Parabens, você ganhou!!")
else:
    print(f"O computador escolheu {sorteio}, e você escolheu: {numero} ente novamente!!")