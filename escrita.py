#Alternativa 1

name = input("Digite o seu nome:\n")
""""
Arquivos mode:
1- opção w - write
1- opção a - append
3- opção r - read
"""
file = open("names.txt", "a")
file.write(f"{name}\n")
file.close()

#Alternativa 2
with open("name.txt", "a") as file:
    file.write(f"{name}\n")