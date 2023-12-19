from abc import ABC, abstractmethod
from typing import List


class Data:
    
    def __init__(self, dia=1, mes=1, ano=2000):
        self.dia = dia
        self.mes = mes
        self.ano = ano

    def __str__(self):
        return f"{self.dia}/{self.mes}/{self.ano}"

    def __eq__(self, outraData):
        return self.dia == outraData.dia and \
               self.mes == outraData.mes and \
               self.ano == outraData.ano
    
    def __lt__(self, outraData):
        if self.ano < outraData.ano:
            return True
        elif self.ano == outraData.ano:
            if self.mes < outraData.mes:
                return True
            elif self.mes == outraData.mes:
                if self.dia < outraData.dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.ano > outraData.ano:
            return True
        elif self.ano == outraData.ano:
            if self.mes > outraData.mes:
                return True
            elif self.mes == outraData.mes:
                if self.dia > outraData.dia:
                    return True
        return False


class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.tipoDeDados = tipoDeDados
        self.lista = []

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def mostraMediana(self):
        pass
    
    @abstractmethod
    def mostraMenor(self):
        pass

    @abstractmethod
    def mostraMaior(self):
        pass
    
    @abstractmethod
    def listarEmOrdem(self):
        pass
    
    @abstractmethod
    def iterar(self):
        pass


    def __str__(self):
        return ', '.join(map(str, self.lista))


class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(str)

    def entradaDeDados(self):
        num_elementos = int(input("Quantos nomes deseja inserir na lista? "))
        for _ in range(num_elementos):
            nome = input("Digite um nome: ")
            self.lista.append(nome)

    def mostraMediana(self):
       
        sorted_lista = sorted(self.lista)
        n = len(sorted_lista)
        mediana = sorted_lista[n // 2]
        
        print(f"Mediana dos nomes: {mediana}")

    def mostraMenor(self):
        print(f"Menor nome: {min(self.lista, key=len)}")

    def mostraMaior(self):
        print(f"Maior nome: {max(self.lista, key=len)}")
        
    def listarEmOrdem(self):
        sorted_lista = sorted(self.lista)
        print(f"{self.tipoDeDados.__name__} em ordem: {sorted_lista}")
        
    def iterar(self, listaSalarios):
        for nome, salario in zip(self.lista, listaSalarios.lista):
            print(f"Nome: {nome}, Salário: R${salario:.2f}")
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(Data)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas datas deseja inserir na lista? "))
        for _ in range(num_elementos):
            dia = int(input("Digite o dia: "))
            mes = int(input("Digite o mês: "))
            ano = int(input("Digite o ano: "))
            data = Data(dia, mes, ano)
            self.lista.append(data)

    def mostraMediana(self):
       
        sorted_lista = sorted(self.lista)
        n = len(sorted_lista)
        mediana = sorted_lista[n // 2]
        
        print(f"Mediana das datas: {mediana}")

    def mostraMenor(self):
        print(f"Menor data: {min(self.lista)}")

    def mostraMaior(self):
        print(f"Maior data: {max(self.lista)}")
        
    def listarEmOrdem(self):
        sorted_lista = sorted(self.lista)
        print(f"{self.tipoDeDados.__name__} em ordem: {sorted_lista}")
        
    def iterar(self):
        for data in self.lista:
            if data.ano < 2019:
                data.dia = 1
            print(f"Data: {data}")

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(float)

    def entradaDeDados(self):
        num_elementos = int(input("Quantos salários deseja inserir na lista? "))
        for _ in range(num_elementos):
            salario = float(input("Digite um salário: "))
            self.lista.append(salario)

    def mostraMediana(self):
      
        sorted_lista = sorted(self.lista)
        n = len(sorted_lista)
       
        if n % 2 == 0:
            mediana = (sorted_lista[n // 2 - 1] + sorted_lista[n // 2]) / 2
        else:
          
            mediana = sorted_lista[n // 2]

        print(f"Mediana dos salários: R${mediana:.2f}")

    def mostraMenor(self):
        print(f"Menor salário: R${min(self.lista):.2f}")

    def mostraMaior(self):
        print(f"Maior salário: R${max(self.lista):.2f}")
        
    def listarEmOrdem(self):
        sorted_lista = sorted(self.lista)
        print(f"{self.tipoDeDados.__name__} em ordem: {sorted_lista}")
        
    def iterar(self):
        salarios_reajustados = map(lambda salario: salario * 1.10, self.lista)
        for salario, salario_reajustado in zip(self.lista, salarios_reajustados):
            print(f"Salário: R${salario:.2f}, Salário Reajustado: R${salario_reajustado:.2f}")


class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(int)

    def entradaDeDados(self):
        num_elementos = int(input("Quantas idades deseja inserir na lista? "))
        for _ in range(num_elementos):
            idade = int(input("Digite uma idade: "))
            self.lista.append(idade)

    def mostraMediana(self):
       
        sorted_lista = sorted(self.lista)
        n = len(sorted_lista)
        mediana = sorted_lista[n // 2]
        
        print(f"Mediana das idades: {mediana} anos")

    def mostraMenor(self):
        print(f"Menor idade: {min(self.lista)} anos")

    def mostraMaior(self):
        print(f"Maior idade: {max(self.lista)} anos")
        
    def listarEmOrdem(self):
        sorted_lista = sorted(self.lista)
        print(f"{self.tipoDeDados.__name__} em ordem: {sorted_lista}")
        
    def iterar(self):
        for idade in self.lista:
            print(f"Idade: {idade} anos")

def incluir_nome(lista_nomes: ListaNomes):
    nome = input("Digite um nome: ")
    lista_nomes.lista.append(nome)

def incluir_salario(lista_salarios: ListaSalarios):
    salario = float(input("Digite um salário: "))
    lista_salarios.lista.append(salario)

def incluir_data(lista_datas: ListaDatas):
    dia = int(input("Digite o dia: "))
    mes = int(input("Digite o mês: "))
    ano = int(input("Digite o ano: "))
    data = Data(dia, mes, ano)
    lista_datas.lista.append(data)

def incluir_idade(lista_idades: ListaIdades):
    idade = int(input("Digite uma idade: "))
    lista_idades.lista.append(idade)

def percorrer_listas(lista_nomes: ListaNomes, lista_salarios: ListaSalarios):
    lista_nomes.iterar(lista_salarios)

def calcular_folha_com_reajuste(lista_salarios: ListaSalarios):
    salarios_reajustados = map(lambda salario: salario * 1.10, lista_salarios.lista)
    for salario, salario_reajustado in zip(lista_salarios.lista, salarios_reajustados):
        print(f"Salário: R${salario:.2f}, Salário Reajustado: R${salario_reajustado:.2f}")

def modificar_dia_datas_antes_2019(lista_datas: ListaDatas):
    for data in lista_datas.lista:
        if data.ano < 2019:
            data.dia = 1
        print(f"Data: {data}")

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas: List[AnaliseDados] = [nomes, datas, salarios, idades]

    while True:
        print("\nMenu de Opções:")
        print("1. Incluir um nome na lista de nomes")
        print("2. Incluir um salário na lista de salários")
        print("3. Incluir uma data na lista de datas")
        print("4. Incluir uma idade na lista de idades")
        print("5. Percorrer as listas de nomes e salários")
        print("6. Calcular o valor da folha com um reajuste de 10%")
        print("7. Modificar o dia das datas anteriores a 2019")
        print("8. Sair")

        opcao = int(input("Escolha uma opção entre 1 e 8  "))

        if opcao == 1:
            incluir_nome(nomes)
        elif opcao == 2:
            incluir_salario(salarios)
        elif opcao == 3:
            incluir_data(datas)
        elif opcao == 4:
            incluir_idade(idades)
        elif opcao == 5:
            percorrer_listas(nomes, salarios)
        elif opcao == 6:
            calcular_folha_com_reajuste(salarios)
        elif opcao == 7:
            modificar_dia_datas_antes_2019(datas)
        elif opcao == 8:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()