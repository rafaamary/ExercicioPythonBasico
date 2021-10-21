''' Escreva um programa que leia a quantidade de dias, horas,
minutos e segundos do usuário. Calcule o total em segundos.'''


qtdDias = int(input('Quantidade de dias: '))
qtdHoras = int(input('Quantidade de horas: '))
qtdMinutos = int(input('Quantidade de minutos: '))
qtdSegundos = int(input('Quantidade de segundos: '))

qtdDiasSeg = ((qtdDias * 24) * 60) * 60
qtdHorasSeg = (qtdHoras * 60) * 60
qtdMinutosSeg = qtdMinutos * 60

soma = qtdDiasSeg + qtdHorasSeg + qtdMinutosSeg + qtdSegundos

print(soma, ' segundos')