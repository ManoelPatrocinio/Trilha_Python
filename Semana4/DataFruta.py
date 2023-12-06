from abc import ABC, abstractmethod
from typing import List

class Data:
    # ... (unchanged)

class AnaliseDados(ABC): 
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados

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
    def __str__(self):
        pass
    @abstractmethod
    def __init__(self, tipoDeDados):
        self.__tipoDeDados = tipoDeDados
        self.__lista = []

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

    def ordenaLista(self):
        self.__lista.sort()
class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []        

    def entradaDeDados(self):
        # Implement input logic for names
        pass

    def mostraMediana(self):
        # Implement median calculation for names
        pass    

    def mostraMenor(self):
        # Implement logic to show the smallest name
        pass

    def mostraMaior(self):
        # Implement logic to show the largest name
        pass

    def __str__(self):
        # Implement logic to represent the object as a string
        pass
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        # Implement input logic for dates
        pass
    
    def mostraMediana(self):
        # Implement median calculation for dates
        pass    
     
    def mostraMenor(self):
        # Implement logic to show the smallest date
        pass
    
    def mostraMaior(self):
        # Implement logic to show the largest date
        pass
    
    def __str__(self):
        # Implement logic to represent the object as a string
        pass

class ListaSalarios(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def entradaDeDados(self):
        # Implement input logic for salaries
        pass

    def mostraMediana(self):
        # Implement median calculation for salaries
        pass    

    def mostraMenor(self):
        # Implement logic to show the smallest salary
        pass

    def mostraMaior(self):
        # Implement logic to show the largest salary
        pass
    
    def __str__(self):
        # Implement logic to represent the object as a string
        pass

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        # Implement input logic for ages
        pass
    
    def mostraMediana(self):
        # Implement median calculation for ages
        pass    
    
    def mostraMenor(self):
        # Implement logic to show the smallest age
        pass
    
    def mostraMaior(self):
        # Implement logic to show the largest age
        pass

    def __str__(self):
        # Implement logic to represent the object as a string
        pass

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    # Iterador zip
    print("\nIterador zip:")
    for nome, salario in zip(nomes, salarios):
        print(f"Nome: {nome}, Salário: {salario}")

    # Iterador map
    print("\nIterador map:")
    novo_salarios = map(lambda x: x * 1.1, salarios)
    for salario in novo_salarios:
        print(f"Salário reajustado: {salario}")

    # Iterador filter
    print("\nIterador filter:")
    datas_ajustadas = filter(lambda x: x.ano < 2019, datas)
    for data in datas_ajustadas:
        # Modificar o dia para o primeiro dia do mês
        data.dia = 1
        print(f"Data ajustada: {data}")
    
    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
