'''
Calculadora tabuada
'''
resultado: int
n = int(input('Qual tabuada você deseja? '))

for i in range(1, 11):
    resultado = n * i
    print(f'{n} x {i}: {resultado} ')