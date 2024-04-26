letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

casos = int(input())

for i in range(casos):
  linha = int(input())
  cont = 0
  for x in range(linha):
    caracter = str(input()).lower().strip()  
    for indice, letra in enumerate(caracter):
      posicao = letras.index(letra)
      cont+=(posicao + indice + x)