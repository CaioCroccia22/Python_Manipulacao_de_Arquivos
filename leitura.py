# enconding="utf-8" para caracteres especiais
with open("dados/names.txt", "r", encoding="utf-8") as file:
    for line in file: #Ler todas as linhas do meu arquivo
        print(f"Olá, {line.rstrip()}")
        # metodo rstrip removes a unsed line
    