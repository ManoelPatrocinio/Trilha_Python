from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia=1, mes=1, ano=2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano

    @property
    def dia(self):
        return self.__dia
    
    @dia.setter
    def dia(self, dia):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        self.__dia = dia

    @property
    def mes(self):
        return self.__mes
    
    @mes.setter
    def mes(self, mes):
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        self.__mes = mes

    @property
    def ano(self):
        return self.__ano
    
    @ano.setter
    def ano(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__ano = ano
    
    def __str__(self):
        return f"{self.__dia:02d}/{self.__mes:02d}/{self.__ano:04d}"

    def __eq__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) == (outraData.__ano, outraData.__mes, outraData.__dia)
    
    def __lt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) < (outraData.__ano, outraData.__mes, outraData.__dia)
    
    def __gt__(self, outraData):
        return (self.__ano, self.__mes, self.__dia) > (outraData.__ano, outraData.__mes, outraData.__dia)


class AnaliseDados(ABC): 

    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__lista = []

    @abstractmethod
    def entradaDeDados(self):
        pass

    @abstractmethod
    def calculaMediana(self):
        pass
    
    @abstractmethod
    def calculaMenor(self):
        pass

    @abstractmethod
    def calculaMaior(self):
        pass

    @abstractmethod
    def listarEmOrdem(self):
        pass

    def __str__(self):
        return str(self.__lista)
    
    def _mediana_indeterminada(self, lista_ordenada):
        meio = len(lista_ordenada) // 2
        if len(lista_ordenada) % 2 == 0:
            # Caso par, retorna o primeiro valor do par
            return lista_ordenada[meio - 1]
        else:
            return lista_ordenada[meio]

    def _calcula_media(self, valor1, valor2):
        return (valor1 + valor2) / 2


class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Quantos nomes deseja inserir na lista? "))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")

        for _ in range(quantidade):
            nome = input("Digite um nome: ")
            self._AnaliseDados__lista.append(nome)

    def calculaMediana(self):
        self._AnaliseDados__lista.sort()
        return self._mediana_indeterminada(self._AnaliseDados__lista)

    def calculaMenor(self):
        return min(self._AnaliseDados__lista)

    def calculaMaior(self):
        return max(self._AnaliseDados__lista)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista)


class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Quantas datas deseja inserir na lista? "))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")

        for _ in range(quantidade):
            dia = int(input("Dia: "))
            mes = int(input("Mês: "))
            ano = int(input("Ano: "))
            data = Data(dia, mes, ano)
            self._AnaliseDados__lista.append(data)

    def calculaMediana(self):
        self._AnaliseDados__lista.sort()
        return self._mediana_indeterminada(self._AnaliseDados__lista)

    def calculaMenor(self):
        return min(self._AnaliseDados__lista)

    def calculaMaior(self):
        return max(self._AnaliseDados__lista)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista, key=lambda x: (x.ano, x.mes, x.dia))


class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Quantos salários deseja inserir na lista? "))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")

        for _ in range(quantidade):
            salario = float(input("Digite um salário: "))
            self._AnaliseDados__lista.append(salario)

    def calculaMediana(self):
        self._AnaliseDados__lista.sort()
        meio = len(self._AnaliseDados__lista) // 2
        if len(self._AnaliseDados__lista) % 2 == 0:
            # Caso par, calcular a média entre os dois valores do meio
            valor1 = self._AnaliseDados__lista[meio - 1]
            valor2 = self._AnaliseDados__lista[meio]
            return self._calcula_media(valor1, valor2)
        else:
            return self._AnaliseDados__lista[meio]

    def calculaMenor(self):
        return min(self._AnaliseDados__lista)

    def calculaMaior(self):
        return max(self._AnaliseDados__lista)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista)


class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))

    def entradaDeDados(self):
        while True:
            try:
                quantidade = int(input("Quantas idades deseja inserir na lista? "))
                break
            except ValueError:
                print("Por favor, insira um número inteiro válido.")

        for _ in range(quantidade):
            idade = int(input("Digite uma idade: "))
            self._AnaliseDados__lista.append(idade)

    def calculaMediana(self):
        self._AnaliseDados__lista.sort()
        meio = len(self._AnaliseDados__lista) // 2
        if len(self._AnaliseDados__lista) % 2 == 0:
            # Caso par, calcular a média entre os dois valores do meio
            valor1 = self._AnaliseDados__lista[meio - 1]
            valor2 = self._AnaliseDados__lista[meio]
            return self._calcula_media(valor1, valor2)
        else:
            return self._AnaliseDados__lista[meio]

    def calculaMenor(self):
        return min(self._AnaliseDados__lista)

    def calculaMaior(self):
        return max(self._AnaliseDados__lista)

    def listarEmOrdem(self):
        return sorted(self._AnaliseDados__lista)
    
    # Nova função para modificar datas
    def modificaDatas(self):
        for data in self._AnaliseDados__lista:
            if data.ano < 2019:
                data.dia = 1

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        print(f"Mediana: {lista.calculaMediana()}")
        print(f"Menor: {lista.calculaMenor()}")
        print(f"Maior: {lista.calculaMaior()}")
        print(f"Lista em ordem: {lista.listarEmOrdem()}")
        print("___________________")

    # Iterador zip: Percorra as listas de nomes e salários
    for nome, salario in zip(nomes.listarEmOrdem(), salarios.listarEmOrdem()):
        print(f"Nome: {nome}, Salário: {salario}")

    # Iterador map: Percorra a lista de salários e calcule o custo da folha de pagamento com reajuste de 10%
    custo_folha = sum(map(lambda salario: salario * 1.1, salarios.listarEmOrdem()))
    print(f"Custo da folha de pagamento com reajuste de 10%: {custo_folha}")

    # Aplica a modificação nas datas da ListaIdades
    idades.modificaDatas()
    print(f"Lista de datas após modificação: {idades.listarEmOrdem()}")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()
