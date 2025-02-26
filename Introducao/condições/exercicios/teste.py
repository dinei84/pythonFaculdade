numero = str(input("Digite um número: "))

# Converter o número em uma lista de dígitos
numerodividido = list(numero)

# Calcular a posição de cada dígito
tamanho = len(numerodividido)

# Imprimir os resultados
for i, digito in enumerate(reversed(numerodividido)):
    if i == 0:
        print(f"Unidade: {digito}")
    elif i == 1:
        print(f"Dezena: {digito}")
    elif i == 2:
        print(f"Centena: {digito}")
    elif i == 3:
        print(f"Milhar: {digito}")
    elif i == 4:
        print(f"Dez milhar: {digito}")
    # Adicione mais condições para números maiores se necessário
