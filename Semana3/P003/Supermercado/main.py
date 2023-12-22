import os


produtos = []

def limpar_tela():
    os.system('clear' if os.name == 'posix' else 'cls')

def inserir_produto():
    codigo = input("Digite o código do produto (13 dígitos): ")
    while len(codigo) != 13 or not codigo.isdigit():
        print("Código inválido. Deve conter 13 dígitos numéricos.")
        codigo = input("Digite o código do produto (13 dígitos): ")

    nome = input("Digite o nome do produto: ")
    while not nome[0].isupper():
        print("O nome do produto deve começar com uma letra maiúscula.")
        nome = input("Digite o nome do produto: ")

    preco = input("Digite o preço do produto: ")
    while not preco.replace('.', '', 1).isdigit():
        print("Preço inválido. Use o formato correto (por exemplo, 12.34).")
        preco = input("Digite o preço do produto: ")

    produto = {'codigo': codigo, 'nome': nome, 'preco': float(preco)}
    produtos.append(produto)
    print("Produto cadastrado com sucesso!")

def excluir_produto():
    codigo = input("Digite o código do produto a ser excluído: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            produtos.remove(produto)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def listar_produtos():
    limpar_tela()
    print("Lista de Produtos:")
    for i, produto in enumerate(produtos, 1):
        print(f"{i}. Código: {produto['codigo']}, Nome: {produto['nome']}, Preço: R${produto['preco']:.2f}")

def consultar_preco():
    codigo = input("Digite o código do produto para consultar o preço: ")
    for produto in produtos:
        if produto['codigo'] == codigo:
            print(f"O preço de {produto['nome']} é R${produto['preco']:.2f}")
            return
    print("Produto não encontrado.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Inserir novo produto")
        print("2. Excluir produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar preço de um produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")
        limpar_tela()

        if opcao == '1':
            inserir_produto()
        elif opcao == '2':
            excluir_produto()
        elif opcao == '3':
            listar_produtos()
        elif opcao == '4':
            consultar_preco()
        elif opcao == '0':
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            
if __name__ == "__main__":
    menu()

