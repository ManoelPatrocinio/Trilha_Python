
def reajusta_dez_porcento(lista_empregados):
    for empregado in lista_empregados:
        empregado['salario'] *= 1.1

def ler_arquivo_e_armazenar_lista(nome_arquivo):
    lista_empregados = []
    with open(nome_arquivo, 'r') as arquivo:
        for linha in arquivo:
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


def exibir_informacoes(lista_empregados):
    for empregado in lista_empregados:
        print(f"Nome: {empregado['nome']} {empregado['sobrenome']}")
        print(f"Ano de Nascimento: {empregado['ano_nascimento']}")
        print(f"RG: {empregado['RG']}")
        print(f"Ano de Admissão: {empregado['ano_admissao']}")
        print(f"Salário: R${empregado['salario']:.2f}")
        print("\n")


if __name__ == "__main__":
    arquivo_funcionarios = "funcionarios.txt"

    lista_funcionarios = ler_arquivo_e_armazenar_lista(arquivo_funcionarios)


    print("Informações antes do reajuste:")
    exibir_informacoes(lista_funcionarios)

   
    reajusta_dez_porcento(lista_funcionarios)

    print("\nInformações após o reajuste:")
    exibir_informacoes(lista_funcionarios)