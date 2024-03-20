from contact import Contact
from exercicio_agenda import contact_book
import csv

Contatos = []

while True:
    print("\n---------------Escolha uma das opções----------------------")
    print("\n 1. Criar o arquivo")
    print("\n 2. Adicionar contato ao documento")
    print("\n 3. Remover contato do documento")
    print("\n 4. Listar os contatos do documento")
    print("\n 5. Sair")
    option = input("Digite qual opção você deseja:\n")
    if option == '1':  # Convertendo para string
        with open('dados/contatos.csv', 'w', newline='', encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(['Nome', 'Número'])  # Cabeçalho do CSV
    elif option == '2':
        name = input("Digite o nome do contato: \n")
        number = input("Digite o número do contato: \n")
        contact = Contact(name, number)
        Contatos.append(contact)  # Adicionando o contato à lista de contatos
        Agenda = contact_book()
        Agenda.addContact(contact)


        
        with open("dados/contatos.csv", "a", encoding="utf-8") as file:
             writer = csv.writer(file, lineterminator='\n')
             writer.writerows(Agenda[name, number])
        print("Contato adicionado com sucesso!")
    elif option == '3':
        name = input("Digite o nome do contato que deseja remover: \n")
        contact = next((c for c in Contatos if c.name == name), None)
        if contact:
            Contatos.remove(contact)  # Removendo o contato da lista de contatos
            Agenda = contact_book()
            Agenda.removeContact(contact)  # Removendo o contato do livro de contatos
            print("Contato removido com sucesso!")
        else:
            print("Contato não encontrado.")
    elif option == '4':
        print("Lista de contatos:")
        for contact in Contatos:
            print(contact)
    elif option == '5':
        print("Saindo...")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")