''' Escreva uma expressão para determinar se uma pessoa deve ou não pagar imposto. Considere 
que pagam imposto pessoas cujo salário é maior que R$ 1.200,00.
'''

salario = float(input('Digite seu salário: '))
pagarImposto = salario > 1200
print('Vai pagar imposto: ', pagarImposto)