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


from contact import Contact
class contact_book:
    def __init__(self):
        self.contact_dict = {}

    def addContact(self, contact):
        self.contact_dict[contact.name] = contact.number

    def listContact(self):
        print(self.contact_dict)
    
    def removeContact(self, contact):
        if contact.name in self.contact_dict:
            del self.contact_dict[contact.name]
        else:
            print("Contato não existe")

Caio = Contact("Caio", "123342353453")
Ana = Contact("Ana", "39120391283")
Mateus = Contact("Mateus", "3490234023")
Agenda = contact_book()
Agenda.addContact(Caio)
Agenda.addContact(Ana)
Agenda.listContact()
Agenda.removeContact(Caio)
Agenda.addContact(Mateus)
Agenda.listContact()