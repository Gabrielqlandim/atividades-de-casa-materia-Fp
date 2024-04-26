def triangulo(A,B,C):
  lista = [float(A),float(B),float(C)]
  lista.sort(reverse = True)
  A,B,C = lista
  valor = []
  if A>= B + C:
     valor.append('NAO FORMA TRIANGULO')
  else: 
    if A*A == B*B + C*C:
      valor.append('TRIANGULO RETANGULO')
    if A*A> B*B + C*C:
      valor.append('TRIANGULO OBTUSANGULO') 
    if A*A < B*B + C*C:
      valor.append('TRIANGULO ACUTANGULO')
    if A == B == C:
      valor.append('TRIANGULO EQUILATERO')
    elif A==B or B==C or A==C:
      valor.append('TRIANGULO ISOSCELES')
  return valor

A,B, C = input().split()
triangulos = triangulo(A,B,C)
for respostas in triangulos:
  print(respostas)
