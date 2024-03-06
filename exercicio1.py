""""
Lendo linhas de um arquivo 
- Escreva um programa para ler as primeiras n linhas de um arquivo
1 - O nome do arquivo e a quantidade de linhas devem ser passadas via parametros na função

"""

def ReadLines(fileName, lines):
    from itertools import islice
    with open(fileName, 'r', encoding="utf-8") as file:
            for line in islice(file, lines):
                  print(line)
            

ReadLines("dados/text.txt", 3)