'''
Calculadora temperatura da carne
'''

temp_celsius = int(input('Qual é a temperatura da carne?: '))

if temp_celsius < 48:
    print('Assar por mais um tempo')
elif temp_celsius in range(46, 53):
    print('Selada')
elif temp_celsius in range(54, 59):
    print('Ao ponto para mal')
elif temp_celsius in range(60, 64):
    print('Ao ponto')
elif temp_celsius in range(65, 70):
    print('Ao ponto para o bem')
elif temp_celsius == 71:
    print('Bem passada')
else:
    print('Queimada')













