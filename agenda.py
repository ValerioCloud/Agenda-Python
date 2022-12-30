def menu():
    voltarMenuPrincipal = 's'
    while voltarMenuPrincipal == 's':
      opcao= input('''
  ======================================================================================================================

                                      PROJETO AGENDA NSTI RIBEIRÃO PRETO

  MENU:

  [1]CADASTRAR CONTATO
  [2]LISTAR CONTATO
  [3]DELETAR CONTATO
  [4]BUSCAR CONTATO PELO NOME
  [5]SAIR
  [6]Listar em ordem alfabética

  =====================================================================================================================
  ESCOLHA UMA OPÇÃO ACIMA:   ''')
      if opcao =="1":
          cadastrarContato()
      elif opcao =="2":
          listarContato()          
      elif opcao =="3":
          deletarContato()
      elif opcao =="4":
          buscarContato()
            
      
      else:
       sair()
      voltarMenuPrincipal=input("DESEJA VOLTAR AO MENU PRINCIPAL ? (S/N) ").lower()    


def cadastrarContato():
  idContato = input("ESCOLHA O ID DO CONTATO: ")
  nome = input("ESCREVA O NOME DO CONTATO: ")
  ramal = input("ESCREVA O RAMAL DO CONTATO: ")
  nucleo = input("ESCREVA O NUCLEO DO CONTATO: ")
  try:
    agenda = open ("agenda.txt","a")
    dados = f'{idContato};{nome};{ramal};{nucleo} \n'
    agenda.write(dados)
    agenda.close()
    print(f'CONTATO GRAVADO COM SUCESSO !!!')
  except:
    print("ERRO NA GRAVAÇÃO DO CONTAO")

def listarContato():
     agenda = open ("agenda.txt","r")     
     for contato in agenda:
      agenda
      print(contato)
     agenda.close()  

def deletarContato():
    nomeDeletado = input("DIGITE O NOME DO USUÁRIO A SER DELETADO:  ").lower()
    agenda = open("agenda.txt","r")
    aux = []
    aux2 = []
    for i in agenda:
      aux.append(i)
    for i in range(0, len(aux)):
      if nomeDeletado not in aux[i].lower():
        aux2.append(aux[i])
    agenda = open("agenda.txt", "w")
    for i in aux2:
      agenda.write(i)
    print(f'CONTATO DELETADO COM SUCESSO')
    listarContato()

  

def buscarContato():
    nome = input (f'DIGITE O NOME A SER PROCURADO: ').upper()
    agenda = open ("agenda.txt","r")
    for contato in agenda:
      if nome in contato.split (";")[1].upper():
       print (contato)
       break
    else:
      print(f'Nome: {nome} não encontrado')
    agenda.close()

    
def sair():
  print (f'Até mais.... !!!')



def main():
    menu()
main()

