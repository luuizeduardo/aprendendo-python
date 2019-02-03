altura = float(input('Altura da parede: '))
largura = float(input('Largura da parede: '))
area = altura * largura
print('A área da parede é de {}m, você precisará de {} litros de tinta'.format(area, (area / 2)))