from random import randint
num = randint(0, 5)
numero_digitado = int(input('Tente adivinha o número que estou pensando (dica: de 0 a 5) '))
if num == numero_digitado:
    print('UAU! Parabéns, você acertou!')
else:
    print(':P Você errou, o número correto era {}'.format(num))