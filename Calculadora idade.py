from datetime import datetime

def calcular_idade(data_nascimento):
    # Obter a data atual
    data_atual = datetime.now()

    # Converter a string de data de nascimento para um objeto datetime
    data_nascimento = datetime.strptime(data_nascimento, '%d/%m/%Y')

    # Calcular a diferença entre as datas
    diferenca = data_atual - data_nascimento

    # Extrair anos, meses e dias da diferença
    anos = diferenca.days // 365
    meses = (diferenca.days % 365) // 30
    dias = (diferenca.days % 365) % 30

    # Calcular o total de meses e dias
    total_meses = diferenca.days // 30
    total_dias = diferenca.days

    return anos, meses, dias, total_meses, total_dias

# Exemplo de uso
data_nascimento = input("Data de nascimento: ")
anos, meses, dias, total_meses, total_dias = calcular_idade(data_nascimento)

print(f"Idade: {anos} anos, {meses} meses e {dias} dias.")
print(f"Total de meses: {total_meses} meses.")
print(f"Total de dias: {total_dias} dias.")