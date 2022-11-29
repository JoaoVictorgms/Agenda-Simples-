
from lib2to3.pgen2.token import RARROW
from mailbox import NotEmptyError



def menu():
    opcao = input('''
    
========================================================
                    AGENDA 
MENU:
[1]CADASTRAR
[2]LISTAR CONTATO
[3]DELETAR CONTATO
[4]BUSCAR CONTATO PELO ID
[5]Sair
    
========================================================
ESCOLHA UMA OPCAO ACIMA 
''')
    if opcao=='1':
        cadastrarContato()
    elif opcao=='2':
        listarContato()
    elif opcao=='3':
        deletarContato()
    elif opcao=='4':
        buscarContatoNome()
    else:
        sair()

def cadastrarContato():
    id = input('Escolha o id :')
    nome = input('Digite seu mome :')
    numero = input('Digite seu numero :')
    email = input('Digite seu email :')
    try:
         agenda = open('agenda.txt','a')
         dados = f'{id};{nome};{numero};{email} \n'
         agenda.write(dados)
         agenda.close()
         print(f'Contato Gravado com Sucesso')
    except:
        print('Error na gravação do contato')


def listarContato():
    agenda  = open('agenda.txt','r')
    for contato in agenda:
        print(contato)
    agenda.close()

def deletarContato():
    nomeDel = input("Insira o nome que deseja deletar")
    agenda = open("agenda.txt",'r')
    aux = []
    aux2 = []
    for i in agenda:
        aux.append(i)
    for i in range(0, len(aux)):
        if nomeDel not in aux[i]:
         aux2.append(aux[i])
    agenda = open("agenda.txt",'w')
    for i in aux2:
        agenda.write(i)
    print(f'contato excluido')
    listarContato() 

            
def buscarContatoNome():
    nome = input("Digite o nome que dejeja bucar:")
    agenda  = open('agenda.txt','r')
    for contato in agenda:
        if nome in contato.split(';')[1]:
            print(contato)
    agenda.close()

def sair():
    print("Até mais")
    exit()

def main():
    menu()

main() 

