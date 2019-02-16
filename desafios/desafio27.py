nome = input('Nome completo: ').strip()
nome_split = nome.split();
print('Nome completo:', nome)
print('Primeiro nome:', nome_split[0])
print('Último nome:', nome_split[len(nome_split) - 1])

