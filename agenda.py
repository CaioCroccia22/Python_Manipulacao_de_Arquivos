""""
Agenda de contatos 
- Desenvolva uma agenda de contatos persistindo as informações em arquivos 
O programa deve seguir as especificidades:
1 - Criar o arquivo Agenda contendo 3 métodos.
    a. Um método para listar contatos.
    b. Um método para adicionar contatos.
    c. Um método para remover contatos.
2 - Criar um arquivo principal para a aplicação que importar o módulo 
de agenda e chamar cada um dos métodos desenvolvidos de acordo com a opção escolhida
"""
import os

def add_contact():
    name = input("Informe o nome: \n")
    address = input("Informe o endereço: \n")
    phone = input("Informe o telefone: \n")

    contact = f"Nome: {name}\nEndereço: {address}\nTelefone: {phone}\n\n"

    with open("dados/contatos.txt", "a", encoding="utf-8") as file:
        file.write(contact)
    
def view_contact():
    if not os.path.exists("dados/contatos.txt"):
        print("Lista de contatos vazia")
        return
    with open("dados/contatos.txt", "r", encoding="utf-8") as file:
        contacts = file.read()
    print("------------Lista de contatos---------------")
    print(contacts)

def delete_contacts():
    if not os.path.exists("dados/contatos.txt"):
        print("Lista de contatos vazia")
        return
    os.remove("dados/contatos.txt")
    print("Contatos excluídos com sucesso")
