agenda = {}

def adicionar_contato(nome, telefone):
    agenda[nome] = telefone
    print("Contato adicionado com sucesso!")

def pesquisar_contato(nome):
    if nome in agenda:
        print(f"Telefone: {agenda[nome]}")
    else:
        print("Contato não encontrado na agenda.")

def remover_contato(nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato removido com sucesso!")
    else:
        print("Contato não encontrado na agenda.")

def listar_contatos():
    if agenda:
        print("--- Contatos na Agenda ---")
        for nome, telefone in agenda.items():
            print(f"Nome: {nome} | Telefone: {telefone}")
    else:
        print("Agenda vazia.")

while True:
    print("\n--- Agenda Telefônica ---")
    print("1. Adicionar contato")
    print("2. Pesquisar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("5. Sair")
    
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(nome, telefone)
    elif opcao == "2":
        nome = input("Digite o nome do contato: ")
        pesquisar_contato(nome)
    elif opcao == "3":
        nome = input("Digite o nome do contato: ")
        remover_contato(nome)
    elif opcao == "4":
        listar_contatos()
    elif opcao == "5":
        break
    else:
        print("Opção inválida. Tente novamente.")
