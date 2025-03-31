class DeliveryApp:
    def __init__(self):
        self.cardapio = {
            1: {"nome": "Hambúrguer", "preco": 15.00},
            2: {"nome": "Pizza", "preco": 25.00},
            3: {"nome": "Salada", "preco": 12.00},
            4: {"nome": "Refrigerante", "preco": 5.00},
            5: {"nome": "Sobremesa", "preco": 10.00}
        }
        self.pedido = []

    def exibir_cardapio(self):
        print("\n--- Cardápio ---")
        for codigo, item in self.cardapio.items():
            print(f"{codigo}. {item['nome']} - R$ {item['preco']:.2f}")
        print()

    def adicionar_ao_pedido(self):
        while True:
            try:
                codigo = int(input("Digite o código do item que deseja adicionar (ou 0 para voltar): "))
                if codigo == 0:
                    break
                if codigo in self.cardapio:
                    self.pedido.append(self.cardapio[codigo])
                    print(f"{self.cardapio[codigo]['nome']} adicionado ao pedido!")
                else:
                    print("Código inválido. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

    def visualizar_pedido(self):
        if not self.pedido:
            print("\nSeu pedido está vazio.")
            return

        print("\n--- Pedido Atual ---")
        total = 0
        for item in self.pedido:
            print(f"- {item['nome']} - R$ {item['preco']:.2f}")
            total += item['preco']
        print(f"Total: R$ {total:.2f}\n")

    def finalizar_pedido(self):
        if not self.pedido:
            print("\nSeu pedido está vazio. Nada para finalizar.")
            return

        print("\nFinalizando o pedido...")
        self.visualizar_pedido()
        print("Pedido finalizado com sucesso! Obrigado por comprar conosco.")
        self.pedido.clear()

    def iniciar(self):
        while True:
            print("\n--- Menu ---")
            print("1. Ver cardápio")
            print("2. Adicionar item ao pedido")
            print("3. Visualizar pedido")
            print("4. Finalizar pedido")
            print("5. Sair")

            try:
                opcao = int(input("Escolha uma opção: "))
                if opcao == 1:
                    self.exibir_cardapio()
                elif opcao == 2:
                    self.adicionar_ao_pedido()
                elif opcao == 3:
                    self.visualizar_pedido()
                elif opcao == 4:
                    self.finalizar_pedido()
                elif opcao == 5:
                    print("Encerrando o programa. Até mais!")
                    break
                else:
                    print("Opção inválida. Tente novamente.")
            except ValueError:
                print("Por favor, insira um número válido.")

# Inicializando o programa
if __name__ == "__main__":
    app = DeliveryApp()
    app.iniciar()