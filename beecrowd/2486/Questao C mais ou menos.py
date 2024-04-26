def comidas(quantidades):
    soma = 0
    for alimento, quantidade in quantidades.items():
        if alimento == 'suco de laranja':
            soma += quantidade * 120
        elif alimento == 'morango fresco' or alimento == 'mamao':
            soma += quantidade * 85
        elif alimento == 'goiaba vermelha':
            soma += quantidade * 70
        elif alimento == 'manga':
            soma += quantidade * 56
        elif alimento == 'laranja':
            soma += quantidade * 50
        elif alimento == 'brocolis':
            soma += quantidade * 34
    return soma

def consumo(soma):
    if 110 <= soma <= 130:
        return f'{soma} mg'
    elif soma < 110:
        quant = 110 - soma
        return f'Mais {quant} mg'
    else:
        quant = soma - 130
        return f'Menos {quant} mg'
    

while True:
    caso = int(input())
    if caso == 0:
        break

    quantidades = {}
    for _ in range(caso):
        entrada = input().split()
        N = int(entrada[0])
        alimento = ' '.join(entrada[1:])
        quantidades[alimento] = N

    soma = comidas(quantidades)
    resultado = consumo(soma)
    print(resultado)
