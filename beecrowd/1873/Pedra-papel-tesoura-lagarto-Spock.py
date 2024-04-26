jogadas = {'pedra':['tesoura', 'lagarto'], 'papel': ['pedra', 'spock'], 'tesoura': ['papel','lagarto'], 'lagarto':['papel', 'spock'], 'spock':['pedra', 'tesoura']}

caso = int(input())
for i in range(caso):
  jogada = str(input()).lower().split()
  if jogada[0]== jogada[1]:
      print('empate')
  elif jogada[1] in jogadas[jogada[0]]:
    print('rajesh')
  else:
    print('sheldon')