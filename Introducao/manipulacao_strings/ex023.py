numero = str(input("Digite um número: "))

numerodividido = list(numero)

unidade = ""
dezena = ""
centena = ""
milhar = ""

if len(numerodividido) == 1:
    unidade = numerodividido[0]
elif len(numerodividido) == 2:
    unidade = numerodividido[1]
    dezena = numerodividido[0]
elif len(numerodividido) == 3:
    unidade = numerodividido[2]
    dezena = numerodividido[1]
    centena = numerodividido[0]
elif len(numerodividido) >= 4:
    unidade = numerodividido[3]
    dezena = numerodividido[2]
    centena = numerodividido[1]
    milhar = numerodividido[0]

# Imprimir os resultados
print("Unidade: ", unidade)
print("Dezena: ", dezena)
print("Centena: ", centena)
print("Milhar: ", milhar)
