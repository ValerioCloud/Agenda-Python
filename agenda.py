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



  =====================================================================================================================
  ESCOLHA UMA OPÇÃO ACIMA: 
  ''')
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
      voltarMenuPrincipal=input("Deseja voltar ao menu principal ? (s/n) ").lower()    


def cadastrarContato():
  idContato = input("Escolha o Id do Contato: ")
  nome = input("Escreva o nome do Contato: ")
  ramal = input("Escreva o ramal do Contato: ")
  nucleo = input("Escreva o nucleo do Contato: ")
  try:
    agenda = open ("agenda.txt","a")
    dados = f'{idContato};{nome};{ramal};{nucleo} \n'
    agenda.write(dados)
    agenda.close()
    print(f'Contato gravado com Sucesso !!!')
  except:
    print("ERRO na gravação do Contato")

def listarContato():
     agenda = open ("agenda.txt","r")
     for contato in agenda:
       print(contato)
     agenda.close()  

def deletarContato():
    nomeDeletado = input("Digite o nome do usuário a ser Deletado:  ").lower()
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
    print(f'Contato deletado com Sucesso')
    listarContato()
    

def buscarContato():
    nome = input (f'digite o nome a ser procurado: ').upper()
    agenda = open ("agenda.txt","r")
    for contato in agenda:
      if nome in contato.split (";")[1].upper():
       print (contato)
    agenda.close()

def sair():
  print (f'Até mais.... !!!')


    


def main():
    menu()
main()

