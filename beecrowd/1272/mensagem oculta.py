casos = int(input())

for i in range(casos):
  letra = str(input()).lower().split()
  letras = []

  for caracter in letra:
    letras.append(caracter[0])

  print(''.join(letras))
