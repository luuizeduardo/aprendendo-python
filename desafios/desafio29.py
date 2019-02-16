velocidade = float(input('Qual a velocidade do carro? '))
if velocidade > 80:
    multa = (velocidade - 80) * 7
    print('Você está acima do limite permitido. Foi gerada uma multa no valor de R$ {:.2f}'.format(multa))
