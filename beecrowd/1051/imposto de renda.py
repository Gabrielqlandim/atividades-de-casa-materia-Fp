def imposto(valor): 
  if valor >= 0 and valor <=2000:
    print('Isento')
  elif valor>=2000.01 and valor<=3000.00:
    calculo = valor*8/100 
    total = (dinheiro-2000)*8/100
    print('R$ {:.2f}'.format(total))
  elif valor>=3000.01 and valor<= 4500:
    calculo = valor*18/100
    total = (1000*8/100) + (dinheiro-3000)*18/100 
    print('R$ {:.2f}'.format(total))
  else:
    calculo = valor*28/100
    total = (1000*8/100) + 1500*18/100 + (dinheiro - 4500)*28/100 
    print('R$ {:.2f}'.format(total))

dinheiro = float(input())
imposto(dinheiro)
