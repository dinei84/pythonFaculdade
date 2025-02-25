nome = str(input("digite seu nome: "))


print("Seu nome em maiusculas: ", nome.upper())
print("Seu nome em minusculas é: ", nome.lower())

nomesemespacos = nome.replace(' ','')
nome2 = len(nomesemespacos)
print("Seu nome tem: ",nome2 , " letras")

nomedivisao = nome.split()
divisao = nomedivisao[0]
divisaocerta = len(divisao)
print("Seu primeiro nome tem: ",  divisaocerta , " letras")

print("Ola!, ", nome)