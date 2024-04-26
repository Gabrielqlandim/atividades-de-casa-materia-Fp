LED = {'1': 2, '2': 5, '3': 5, '4': 4, '5': 5, '6': 6, '7': 3, '8': 7, '9': 6, '0': 6}

total = int(input())
for i in range(total):
  numero = input()
  cont = 0
  for led in numero:
    cont+=LED[led]
  print(f'{cont} leds')