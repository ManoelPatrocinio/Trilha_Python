# Função para reajustar o salário em 10%
def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.1

# Função para ler informações dos funcionários de um arquivo e armazenar em uma lista
def ler_arquivo_e_armazenar_dados(nome_arquivo):
    lista_empregados = []
    with open(nome_arquivo, 'r') as arquivo:
        linhas = arquivo.readlines()
        for linha in linhas:
            dados = linha.strip().split(',')
            empregado = {
                'nome': dados[0],
                'sobrenome': dados[1],
                'ano_nascimento': int(dados[2]),
                'RG': dados[3],
                'ano_admissao': int(dados[4]),
                'salario': float(dados[5])
            }
            lista_empregados.append(empregado)
    return lista_empregados

# Função para exibir os dados dos empregados
def exibir_dados(lista_empregados):
    for empregado in lista_empregados:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}, Ano de Nascimento: {empregado['ano_nascimento']}, RG: {empregado['RG']}, Ano de Admissão: {empregado['ano_admissao']}, Salário: R${empregado['salario']:.2f}")

# Aplicativo para testar a função
if __name__ == "__main__":
    # Nome do arquivo com as informações dos empregados
    arquivo_empregados = 'empregados.txt'

    # Lê as informações do arquivo e armazena na lista
    lista_empregados = ler_arquivo_e_armazenar_dados(arquivo_empregados)

    # Exibe os dados antes do reajuste
    print("Dados dos empregados antes do reajuste:")
    exibir_dados(lista_empregados)

    # Aplica o reajuste de 10% nos salários
    reajusta_dez_porcento(lista_empregados)

    # Exibe os dados após o reajuste
    print("\nDados dos empregados após o reajuste:")
    exibir_dados(lista_empregados)
