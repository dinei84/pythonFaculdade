frase = 'Curso em Video Python'

# FATIAMENTO    
#print(frase[9:21:2]) #9 é o começo, 21 é o fim, e 2 é p passo
#print(frase[:15:3]) # do 0 ao 15 com passo 3

# ANALISE
#print(len(frase)) # comprimento da frase
#print(frase.lower().count('p')) #combinação de dois metodos
#print(frase.lower().find('py')) #enconstrando py minusculo
#print('em' in frase) #encontrando em na frase

#TRANSFORMAÇÃO
#print(frase.replace('Python', 'Android')) #substituindo uma frase por outra
#print(frase.title()) #deixa todos os  começos de palavras com maiusculas

frase2 = '  Curso em Video   '

#print(frase2.strip()) #elimina os espaços exedentes das estremidades
#print(frase2.rstrip()) #elimina os espaços exedentes da direita
#print(frase2.lstrip()) #elimina os espaços exedentes da esquerda

#DIVISÃO
#print(frase.split()) #remove os espaços internos da frase, transformando as novas frases em novas listas

#JUNÇÃO
#print('-'.join(frase)) #adiciona uma - antes e depois de cada letra (menos as ultimas)

print(frase.find(' '), frase.replace(' ', '-')) #procurando todos os espaços e substituindo por -