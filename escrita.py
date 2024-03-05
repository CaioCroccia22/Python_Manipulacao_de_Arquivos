name = input("Digite o seu nome:\n")
""""
Arquivos mode:
1- opção w - write
1- opção a - append
3- opção r - read
"""
file = open("names.txt", "a")
file.write(name)
file.close()