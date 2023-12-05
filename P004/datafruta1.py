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
        return "{}/{}/{}".format(self.__dia, self.__mes, self.__ano)

    def __eq__(self, outraData):
        return self.__dia == outraData.__dia and \
               self.__mes == outraData.__mes and \
               self.__ano == outraData.__ano
    
    def __lt__(self, outraData):
        if self.__ano < outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes < outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia < outraData.__dia:
                    return True
        return False
    
    def __gt__(self, outraData):
        if self.__ano > outraData.__ano:
            return True
        elif self.__ano == outraData.__ano:
            if self.__mes > outraData.__mes:
                return True
            elif self.__mes == outraData.__mes:
                if self.__dia > outraData.__dia:
                    return True
        return False


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
            try:
                # Divida a entrada em partes (dia, mês, ano)
                dia, mes, ano = map(int, input("Digite a data no formato dia/mês/ano: ").split('/'))
                data = Data(dia, mes, ano)
                self._AnaliseDados__lista.append(data)
            except ValueError:
                print("Formato de data inválido. Por favor, use o formato dia/mês/ano.")

    def calculaMediana(self):
        self._AnaliseDados__lista.sort()
        return self._mediana_indeterminada(self._AnaliseDados__lista)

    def calculaMenor(self):
        return min(self._AnaliseDados__lista)

    def calculaMaior(self):
        return max(self._AnaliseDados__lista)


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
        print("___________________")

    print("Fim do teste!!!")


if __name__ == "__main__":
    main()
