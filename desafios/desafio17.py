from math import hypot
cateto_oposto = int(input('Informe o cateto oposto: '))
cateto_ad = int(input('Informe o cateto adjacente: '))
print('A hipotenusa de {} e {} é {}'.format(cateto_oposto, cateto_ad, hypot(cateto_oposto, cateto_ad)))