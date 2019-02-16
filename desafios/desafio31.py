km = int(input('Digite a quantidade de KM da viagem '))
if km >= 200:
    preco = km * 0.45
    print('O preço por KM é R$ 0,45. Você precisa pagar {:.2f}'.format(preco))
else:
    preco = km * 0.5
    print('O preço por KM é R$ 0,50. Você precisa pagar {:.2f}'.format(preco))