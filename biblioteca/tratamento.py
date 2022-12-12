def ler_dados(file):
    coluna = []
    dado = open(file)
    linhas = dado.readlines()
    for i in linhas:
        tam = len(i)
        coluna.append(i[:tam-1])
    return coluna
     
