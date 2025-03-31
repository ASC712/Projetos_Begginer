'''
Calculadora IMC
'''

altura = float(input('Qual a sua altura em cm?: '))
peso = float(input('Qual o seu peso?: '))
imc = peso / (altura/100)**2

if imc < 18.5:
    print('Magreza')
elif imc >= 18.5 and imc < 24.9:
    print('Normal')
elif imc >= 25.0 and imc < 29.9:
    print('Sobrepeso')
elif imc >= 30.0 and imc < 39.9:
    print('Obesidade')
else:
    print('Obesidade grave')