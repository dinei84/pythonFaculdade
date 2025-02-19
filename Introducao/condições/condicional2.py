velocidade = int(input("Digite a velocidade do veiculo: "))

multa = (velocidade - 80) * 7

if velocidade > 80:
    print(f"Sua velociade era de {velocidade}Km/h, e foi multado!!!, sua multa é de R${multa},00")
else:
    print("Pode viajar!!")