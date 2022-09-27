listaEleitores= []
listaCandidatos=[]

eleitores = 0
votaram = 0
votos= 0
branco=0
qtd_canditatos= int(input("Quantidade de canditatos: "))


for i in range(qtd_canditatos):
    nome = input ("CANDIDATO: ")
    ID = int(input ("NÚMERO: "))
    Part = input("PARTIDO:")
    listaCandidatosAtual={'nome': nome, 'numero': ID, 'partido':Part, 'votos':0}
    listaCandidatos.append(listaCandidatosAtual)
    print("########################")


print("BEM VINDO(A) URNA ELETRONICA , ESCOLHA UMA DAS OPÇÕES\n")

print("""
   1) Cadastrar eleitor;
   2) Listar eleitores;
   3) Listar candidatos;
   4) Alterar candidato;
   5) Votar em algum candidato;
   6) Votos obtidos por candidato;
   7) Eleitores que já votaram;
   8) Eleitores que ainda não votaram;
   9) Sair da Urna Eletrônica""")

while True:
  menu = int(input("Escolha uma opção:"))
  if menu == 1:
    nome = input("digite o nome do eleitor: ")
    cpf = int(input("digite o cpf: "))
    
    eleitor={'nome': nome, 'cpf': cpf, 'votou': False}
    listaEleitores.append(eleitor)
    eleitores+=1
    print("Cadastrado com sucesso")
    print(listaEleitores)

  elif menu == 2:
    print("Lista de eleitores: ")
    for eleitor in listaEleitores:
      
      print(eleitor)

  elif menu == 3:
    for candidato in listaCandidatos:
      print("lista candidatos: ")
      print(candidato)

  elif menu == 4:
    candidato = int(input("Número do candidato deseja alterar: "))
    for can in listaCandidatos:
      if can['numero'] == candidato:
        escolha = input(" Deseja alterar o nome e/ou partido: [nome] [partido] [ambos]")
        if escolha == "nome":
          novo_nome= input("Novo nome: ")
          can['nome'] = novo_nome
        elif escolha == "partido":
          novo_partido = input("Novo partido: ")
          can["partido"] = novo_partido
        elif escolha == "ambos":
           novo_nome= input("Novo nome: ")
           novo_partido = input("Novo partido: ")
           can["partido"] = novo_partido
           can['nome'] = novo_nome
        print("Alterado com sucesso")
  elif menu == 5:

    branco = input("Deseja votar branco? [s/n]: ")
    nulo = input("Deseja votar nulo? [s/n]: ")
    cpf = int(input("informe seu cpf: "))
    for eleitor in range(listaEleitores):
      print(eleitor["cpf"])
      if eleitor['cpf']  == cpf: 
          
          if eleitor["votou"] == True:
              print("Eleitor já votou...")
              break
          else:
              if branco=="s" or nulo =="s":
                eleitor["votou"] = True
                print("Eleitor votou branco ou nulo...")
                break
              else:
                num = int(input(" numero do candidato: "))
                eleitor["votou"] = True
                for candidato in listaCandidatos:
                    if candidato["numero"] == num:
                      candidato["votos"] += 1
                      votos+=1
                      votaram +=1
               
      else:
          print("Eleitor não encontrado...")
          break
            

  elif  menu == 6:
     num = int(input( "numero do candidato: "))
     for candidato in listaCandidatos:
       if candidato['numero'] == num:
         print("Votos obtidos pelo candidato ", candidato["votos"])

  elif menu == 7:
    print("Já votaram", votos, "pessoas")
  elif menu == 8:
    print("Não votaram",(eleitores - votaram))

  elif menu == 9 :
    print("Saindoo...")
    break
