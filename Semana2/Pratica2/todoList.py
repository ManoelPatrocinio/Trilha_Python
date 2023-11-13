import os
todoList = []
finishList = []


def registraTarefa():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    novaTodo = input("Adicione um tarefa: ")
    todoList.append(novaTodo)
    print("\nTarefa registrada!!!\n")

  
def listarTarefas():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if len(finishList) > 0:
        for index, item in enumerate(finishList):
            try:
                print(index + 1,".", item, "[x]")
                
            except Exception as inst:
                print ("Ocorreu um erro!",inst)
    for index, item in enumerate(todoList):
        try:
            id = len(finishList) + (index + 1)
            print(id,".", item, "[ ]")
            
        except Exception as inst:
            print ("Ocorreu um erro!",inst)
    
def concluirTarefa():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    listarTarefas()
    id = input("Informe o identificador da tarefa: ")
    
    for i in range(len(todoList)):
        if(i ==  (int(id) - 1)):
          finishList.append(todoList[i])
          todoList.pop(i)
          print("Tarefa localizada: ", todoList[i])
          print("Tarefa concluida !!! ")
        
def Menu():
    
    print("\n\n1 - P/ Adicionar tarefa")
    print("2 - P/ Concluir tarefa")
    print("3 - P/ Listar tarefa")
    print("0 - P/ Sair")
    escolha = input("Sua escolha: ")
    
    return escolha
    
def main():
    while True:
        esc = Menu()
        match esc:
            case "1":
                registraTarefa()
            case "2":
                concluirTarefa()
            
            case "3":
                listarTarefas()
            case "0": 
                return   
                

main()
           