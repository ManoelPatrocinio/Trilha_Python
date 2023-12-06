import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def insert_product(products):
    code = input("Digite o código do produto (13 caracteres): ")
    while len(code) != 13 or not code.isdigit():
        print("Código inválido. Deve ter 13 caracteres numéricos.")
        code = input("Digite o código do produto (13 caracteres): ")

    name = input("Digite o nome do produto (começando com letra maiúscula): ")
    while not name[0].isupper():
        print("Nome inválido. Deve começar com letra maiúscula.")
        name = input("Digite o nome do produto (começando com letra maiúscula): ")

    price = input("Digite o preço do produto (com duas casas decimais): ")
    while not price.replace('.', '').isdigit():
        print("Preço inválido. Deve ser um número decimal com duas casas decimais.")
        price = input("Digite o preço do produto (com duas casas decimais): ")

    product = {
        'code': code,
        'name': name,
        'price': float(price)
    }

    products.append(product)
    print("Produto cadastrado com sucesso!")

def delete_product(products):
    code_to_delete = input("Digite o código do produto a ser excluído: ")
    for product in products:
        if product['code'] == code_to_delete:
            products.remove(product)
            print("Produto excluído com sucesso!")
            return
    print("Produto não encontrado.")

def list_products(products):
    if not products:
        print("Nenhum produto cadastrado.")
    else:
        for i, product in enumerate(products, 1):
            print(f"{i}. Código: {product['code']}, Nome: {product['name']}, Preço: R${product['price']:.2f}")

def consult_price(products):
    code_to_consult = input("Digite o código do produto para consultar o preço: ")
    for product in products:
        if product['code'] == code_to_consult:
            print(f"O preço de {product['name']} é R${product['price']:.2f}")
            return
    print("Produto não encontrado.")

def main():
    products = []

    while True:
        clear_screen()
        print("Menu de Opções:")
        print("1. Inserir um novo produto")
        print("2. Excluir um produto cadastrado")
        print("3. Listar todos os produtos")
        print("4. Consultar o preço de um produto")
        print("0. Sair")

        choice = input("Digite a opção desejada: ")

        if choice == '1':
            insert_product(products)
        elif choice == '2':
            delete_product(products)
        elif choice == '3':
            list_products(products)
        elif choice == '4':
            consult_price(products)
        elif choice == '0':
            print("Programa encerrado.")
            break
        else:
            print("Opção inválida. Tente novamente.")

        input("\nPressione Enter para continuar...")

if __name__ == "__main__":
    main()


