def jogadas(P, J1, J2, R, A):
  P = int(P)
  J1 = int(J1)
  J2 = int(J2)
  R = int(R)
  A = int(A)
  if P == 1:
      soma = J1 + J2
      if soma%2 == 1:
        if R == 0 and A == 0:
          print('Jogador 2 ganha!')
        if R == 1 and A == 0:
          print('Jogador 1 ganha!')
        if R == 1 and A == 1:
          print('Jogador 2 ganha!')
        if R== 0 and A == 1:
          print('Jogador 1 ganha!')
      else:
        if R == 0 and A == 0:
          print('Jogador 1 ganha!')
        if R == 1 and A == 0:
          print('Jogador 1 ganha!')
        if R == 1 and A == 1:
          print('Jogador 2 ganha!')
        if R== 0 and A == 1:
          print('Jogador 1 ganha!')
  elif P == 0:
      soma = J1 + J2
      if soma%2 == 1:
        if R == 0 and A == 0:
          print('Jogador 1 ganha!')
        if R == 1 and A == 0:
          print('Jogador 1 ganha!')
        if R == 1 and A == 1:
          print('Jogador 2 ganha!')
        if R== 0 and A == 1:
          print('Jogador 1 ganha!')
      else:
        if R == 0 and A == 0:
          print('Jogador 2 ganha!')
        if R == 1 and A == 0:
          print('Jogador 1 ganha!')
        if R == 1 and A == 1:
          print('Jogador 2 ganha!')
        if R== 0 and A == 1:
          print('Jogador 1 ganha!')


P, J1, J2, R, A = input().split()
jogadas(P, J1, J2, R, A)
