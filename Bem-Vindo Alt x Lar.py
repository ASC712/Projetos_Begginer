# Entrada: N M
N, M = map(int, input('Digite dois valores:').split())

# Parte de cima
for i in range(1, N, 2):
    print(('.|.' * i).center(M, '-'))

# Linha do meio
print('BEM-VINDO'.center(M, '-'))

# Parte de baixo
for i in range(N-2, 0, -2):
    print(('.|.' * i).center(M, '-'))