def parenteses(exp):
    lista = []
    for simb in exp:
      if simb == '(':
        lista.append('(')
      elif simb == ')':
        if len(lista)>0:
          lista.pop()
        else:
          lista.append(')')
          break
    if len(lista) == 0:
      return 'correct'
    else:
      return 'incorrect'

while True:
    try:
        exp = input().strip()

        correct = True
        parenteses = 0

        for letra in exp:
            if(letra == '('):
                parenteses += 1
            elif(letra == ')'):
                if(parenteses > 0):
                    parenteses -= 1
                else:
                    correct = False
                    break
        
        correct = correct and (parenteses == 0)
        
        print("correct" if correct else "incorrect")
    except EOFError:
        break
