import os
import copy
import platform
import locale
from datetime import datetime
locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')
data_e_hora_atual = datetime.now()
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
        if dia < 1 or dia > 31:
            raise ValueError("Dia inválido")
        if mes < 1 or mes > 12:
            raise ValueError("Mês inválido")
        if ano < 1900 or ano > 2100:
            raise ValueError("Ano inválido")
        self.__dia = dia
        self.__mes = mes
        self.__ano = ano
        
    @property
    def year(self):
        return self.__ano
    
    @year.setter
    def year(self, ano):
        if ano < 2000 or ano > 2100:
            raise ValueError("Ano inválido")
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
        return  self.__dia == outraData.__dia and \
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

class ListaNomes(AnaliseDados):
    
    def __init__(self):
        super().__init__(type("String"))
        self.__lista = []
        self.__nomes = []
        self.__salarios = []        

    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        limpaTela() 
        print("\n\t=========== CADASTRO DE NOMES ===========\n")
        
        while True:
            try:
                quantElementos = int(input("\n\tQuantos elementos vão existir na lista: "))
                break  # Se a conversão para int for bem-sucedida, sai do loop
            except ValueError:
                print("\tPor favor, digite um número inteiro válido.")
                pause() 
                limpaTela() 
        
        for i in range(quantElementos):
            while True:
                limpaTela()
                elemento = input("\n\tDigite o elemento {}: ".format(i + 1))
                if elemento.isalpha():
                    self.__lista.append(elemento)
                    break
                else:
                    limpaTela()
                    print("\tPor favor, digite apenas letras.")
                    pause() 
                    limpaTela() 
        pass

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular a mediana.")
            return

        lista_ordenada = sorted(self.__lista)
        tamanho = len(lista_ordenada)

        if tamanho % 2 == 0:
            meio1 = lista_ordenada[tamanho // 2 - 1]
            meio2 = lista_ordenada[tamanho // 2]
            mediana = (meio1, meio2)
        else:
            mediana = lista_ordenada[tamanho // 2]

        print(f"\n\tA mediana da lista é: {mediana[0]}")  # Mostra o primeiro valor na mediana
        pause()
        
        pass    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o menor elemento.")
            return
        
        menor = self.__lista[0]
        for elemento in self.__lista:
            if elemento < menor:
                menor = elemento
        print(f"\n\tO menor elemento da lista é: {menor}")
        pause()
        
        pass

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        
        if not self.__lista:
            print("A lista está vazia. Não é possível calcular o maior elemento.")
            return
        
        maior = self.__lista[0] 
        for elemento in self.__lista:
            if elemento > maior:
                maior = elemento
        print(f"\n\tO maior elemento da lista é: {maior}")
        pause()
        
        pass    

    def listarEmOrdem(self):
        '''
        Este método ordena a lista e mostra os
        elementos em ordem crescente
        '''
        limpaTela()
        if not self.__lista:
            print("A lista está vazia. Não é possível ordenar.")
            return

        lista_ordenada = sorted(self.__lista)
        print("\n\t=========== LISTA DE NOMES EM ORDEM ALFABÉTICA ===========\n")
        for elemento in lista_ordenada:
            print(f"\tNome: {elemento}")
        pause()
        
        pass
    
    def percorreListaDeNomesESalarios(self, outras_nomes, outras_salarios):
        
        if not self.__lista:
            limpaTela() 
            print("\n\tA lista está vazia. Não é possível percorrer a lista de nomes e salários.")
            pause()
            return
        
        limpaTela()
        print("\n\t=========== LISTA DE NOMES E SALÁRIOS ===========\n")
        for nome, salario in zip(self.__lista, outras_salarios._ListaSalarios__lista):
            print("\tNome: {}, Salário: {:.2f}".format(nome, salario))
        pause()
    

        pass
	

        '''
        Este método ordena a lista e mostra os
        elementos em ordem crescente
        '''
        limpaTela()     
        print("\n\t=========== LISTA DE IDADES EM ORDEM CRESCENTE ===========\n")

        lista_ordenada = sorted(self.__lista)
        
        for elemento in lista_ordenada:
            print(f"\tIdade: {elemento}")
        pause()
        pass
    
def pause():
  input("\tPressione Enter para continuar...")
  
def limpaTela():
  sistema_operacional = platform.system().lower()

  if sistema_operacional == "windows":
    os.system("cls")
  elif sistema_operacional == "linux":
    os.system("clear")
  else:
    print("Sistema operacional não suportado para limpar a tela.")

def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalarios()
    idades = ListaIdades()
    nomes.entradaDeDados()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        print("___________________")

    print("Fim do teste!!!")
    
if __name__ == "__main__":
    main()