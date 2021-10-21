'''Escreva um programa que calcule o tempo de uma 
viagem de carro. Pergunte a distância a 
percorrer e a velocidade média esperada para a viagem.'''


distancia = float(input('Qual a distancia a ser percorrida? '))
VelocidadeMed = float(input('Qual a valocidade media?'))
tempoViagem = distancia/VelocidadeMed

print('O tempo de viagem e igual a: ', tempoViagem, ' horas.')