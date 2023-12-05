
from abc import ABC, abstractmethod

class Data:
    
    def __init__(self, dia = 1, mes = 1, ano = 2000):
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
    
	
	
	# Data (int _dia, int _mes, int _ano) {
	# 	dia = _dia;
	# 	mes = _mes;
	# 	ano = _ano;
	# }
	# string toString() {
	# 	string ret = "";
	# 	ret.append(to_string(dia));
	# 	ret.append("/");
	# 	ret.append(to_string(mes));
	# 	ret.append("/");
	# 	ret.append(to_string(ano));
	# 	return ret;
	# }

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

    def getList(self):
        return self.__lista
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles.
        '''
        print("\n\n--- Cadastro de nomes ---\n\n")
        optionQTD = int(input("Quantos nomes deseja cadastrar ? -> "))
        for i in range(optionQTD):
            nome = input(f'Informe o  {i+1}º nome:')
            self.__lista.append(nome)
            nome = ""

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        mediana = ""
        sorted_list = sorted(self.__lista)
        if len(self.__lista) % 2 == 0:
            mediana = sorted_list[(len(self.__lista) // 2) - 1]
        else:
            mediana = sorted_list[(len(self.__lista) // 2)]
        print(f'A mediana da lista de nomes é: {mediana}')

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        menor = min(self.__lista, key=lambda x: len(x.strip()))
        print(f'O menor valor la lista de nomes é: {menor}')


    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        maior = max(self.__lista, key=lambda x: len(x.strip()))
        print(f'O maior valor la lista de nomes é: {maior}')
        
    def listarEmOrdem(self):
        print("--- Lista ordenada de nomes ---")
        
        for item in self.__lista:
            print(f'{item}')
            
             

    def __str__(self):
        pass
	
class ListaDatas(AnaliseDados):
        
    def __init__(self):
        super().__init__(type(Data))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("\n\n--- Cadastro de Datas ---\n\n")
        optionQTD = int(input("Quantas datas deseja informar ? -> "))
        for i in range(optionQTD):
            _dia = int(input("informe o dia ? -> "))
            _mes = int(input("informe o mes ? -> "))
            _ano = int(input("informe o ano ? -> "))
            novaData = Data(_dia,_mes,_ano)

            self.__lista.append(novaData)
    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        mediana = ""
        sorted_list = sorted(self.__lista)
                
        if len(self.__lista) % 2 == 0:
            mediana = sorted_list[(len(self.__lista) // 2) - 1]
        else:
            mediana = sorted_list[(len(self.__lista) // 2)]
        print(f'A mediana da lista de datas é: {mediana}')

    
     
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        menor = min(self.__lista)
        print(f'O menor valor da lista de datas é: {menor}')
    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        maior = max(self.__lista)
        print(f'O maior valor da lista de datas é: {maior}')
    
    def __str__(self):
        pass
    def listarEmOrdem(self):
        print("--- Lista ordenada de datas ---")
        
        for item in self.__lista:
            print(f'{item.__str__()}')

class ListaSalários(AnaliseDados):

    def __init__(self):
        super().__init__(type(float))
        self.__lista = []        

    def getList(self):
        return self.__lista
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("\n\n--- Cadastro de salario ---\n\n")
        optionQTD = int(input("Quantos salários deseja cadastrar ? -> "))
        for i in range(optionQTD):
            salario = float(input(f'Informe o  {i+1}º salario:'))
            self.__lista.append(salario)
            salario = 0

    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        mediana = 0
        
        sorted_list = sorted(self.__lista)
        if len(self.__lista) % 2 == 0:
            try:
                mediana =( sorted_list[(len(self.__lista) // 2)] + sorted_list[((len(self.__lista) // 2))-1] )/ 2
            except ValueError:
                print("Não foi possível realizar o calculo da mediana, da lista com numero par de itens.")
                return
        else:
            try:
                mediana = sorted_list[(len(self.__lista) // 2) - 1]
            except ValueError:
                print("Não foi possível realizar o calculo da mediana, da lista com numero impar de itens.")
                return

        print(f'A mediana da lista de salários é: {mediana}')
    

    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        menor = min(self.__lista)
        print(f'O menor valor da lista de salários é: {menor}')

    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        maior = max(self.__lista)
        print(f'O maior valor da lista de salários é: {maior}')
    
    def __str__(self):
        pass
    def listarEmOrdem(self):
        print("--- Lista ordenada de salarios ---")
        
        for item in self.__lista:
            print(f'{item}')
    def reajuste(self):
        print("--- Custo da folha com reajuste (10%) ---")
        reajusta10 = lambda x: x + ( (x * 10) /100)
        soma = 0
        for sal in map(reajusta10,self.__lista):
            soma += sal
        print(f'custo total apos reajuste: {soma}')   
        

class ListaIdades(AnaliseDados):
    
    def __init__(self):
        super().__init__(type(int))
        self.__lista = []        
    
    def entradaDeDados(self):
        '''
        Este método pergunta ao usuários quantos
        elementos vão existir na lista e depois
        solicita a digitação de cada um deles
        '''
        print("\n\n--- Cadastro de idade ---\n\n")
        optionQTD = int(input("Quantas idades deseja cadastrar ? -> "))
        for i in range(optionQTD):
            idade = int(input(f'Informe a  {i+1}º idade:'))
            self.__lista.append(idade)
            idade = 0

    
    def mostraMediana(self):
        '''
        Este método ordena a lista e mostra o
        elemento que está na metade da lista
        '''
        mediana = 0
        
        sorted_list = sorted(self.__lista)
        if len(self.__lista) % 2 == 0:
            try:
                mediana =( sorted_list[(len(self.__lista) // 2)] + sorted_list[((len(self.__lista) // 2))-1] )/ 2
            except ValueError:
                print("Não foi possível realizar o calculo da mediana, da lista com numero par de idades.")
                return
        else:
            try:
                mediana = sorted_list[(len(self.__lista) // 2) - 1]
            except ValueError:
                print("Não foi possível realizar o calculo da mediana, da lista com numero impar de idades.")
                return

        print(f'A mediana da lista de idade é: {mediana}')    
    
    def mostraMenor(self):
        '''
        Este método retorna o menos elemento da lista
        '''
        menor = min(self.__lista)
        print(f'O menor valor da lista de idades é: {menor}')

    
    def mostraMaior(self):
        '''
        Este método retorna o maior elemento da lista
        '''
        menor = max(self.__lista)
        print(f'O maior valor da lista de idades é: {menor}')

    def __str__(self):
        pass
    def listarEmOrdem(self):
        print("--- Lista ordenada de idades ---")
        
        for item in self.__lista:
            print(f'{item}')


def listaNomeSalario(listaNomes, listaSalarios):
    for nome,salario in zip(listaNomes,listaSalarios):
        print(f"Nome: {nome}  | salario: {salario}")
    

    
def main():
    nomes = ListaNomes()
    datas = ListaDatas()
    salarios = ListaSalários()
    idades = ListaIdades()

    listaListas = [nomes, datas, salarios, idades]

    for lista in listaListas:
        lista.listarEmOrdem()
        lista.entradaDeDados()
        lista.mostraMediana()
        lista.mostraMenor()
        lista.mostraMaior()
        
        print("___________________")

    listaNomeSalario(nomes.getList(),salarios.getList())
    salarios.reajuste()
    print("Fim do teste!!!")

if __name__ == "__main__":
    main()
