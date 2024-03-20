from agenda import add_contact, view_contact, delete_contacts



def main():
    while True:
        print("\n---------------Escolha uma das opções----------------------")
        print("\n 1. Adicionar contato")
        print("\n 2. Visualizar contatos")
        print("\n 3. Excluir todos os contatos")
        print("\n 4. Sair")
        option = input("Digite o número da opção desejada:\n")
        if option == '1':
            add_contact()
        elif option == '2':
            view_contact()
        elif option == '3':
            delete_contacts()
        elif option == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

main()