from biblioteca.tratamento import ler_dados
t = 0
# retorno dos dados dos documentos txt
# formato de retorno --> lista
coluna_obito = ler_dados('dados\coluna_obito.txt')
coluna_sexo = ler_dados('dados\coluna_sexo.txt')
coluna_faixa_etaria =ler_dados('dados\coluna_faixa_etaria.txt')
#variavel de contagem 
# homen ou mulher
# 0-9   <-- vivos ou morto com idade de 0 a 9
# 10-19 <-- vivos ou morto com idade de 10 a 19
# 0-9-v   <-- vivos  com idade de 0 a 9
# 0-9-m   <-- morto com idade de 0 a 9
# 10-19-v   <-- vivos  com idade de 10 a 19
# 10-19-m   <-- morto com idade de 10 a 19

homen ={'0-9':0,
        '0-9-v':0,
        '0-9-m':0,
        '10-19':0,
        '10-19-v':0,
        '10-19-m':0
        }
mulher ={'0-9':0,
        '0-9-v':0,
        '0-9-m':0,
        '10-19':0,
        '10-19-v':0,
        '10-19-m':0
        }

# leitura dos dados e condicionais de contagem se for verdadeira a premissa
for i in range(len(coluna_faixa_etaria)):
    t+=1
    #===========================================
    #===========================================
    #===========================================
    #   pergunta 1
    #  - qual o sexo - homen
    #===========================================
    if coluna_sexo[i] == 'Homem':
    #   pergunta 2 - qual a faixa etaria 0 a 9
        if coluna_faixa_etaria[i] == '0 a 9':
            homen['0-9']+=1
    #   pergunta 3
    #   qtds obito sim
            if coluna_obito[i] == 'Sim':
               homen['0-9-m']+=1
                
    #   pergunta 3
    #   qtds obito não
            else:
                homen['0-9-v']+=1
    #===========================================
    #   pergunta 2
    #  - qual a faixa etaria 10 a 19
        if coluna_faixa_etaria[i] == '10 a 19':
            homen['10-19']+=1
    #   pergunta 3
    #   qtds obito sim
            if coluna_obito[i] == 'Sim':
                homen['10-19-m']+=1
    #   pergunta 3
    #   qtds obito não
            else:
                homen['10-19-v']+=1

    #===========================================
    #===========================================
    #===========================================
    #   pergunta 1
    #  - qual o sexo - mulher
    #===========================================
    if coluna_sexo[i] == 'Mulher':
    #   pergunta 2 - qual a faixa etaria 0 a 9
        if coluna_faixa_etaria[i] == '0 a 9':
            mulher['0-9']+=1
            if coluna_obito[i] == 'Sim':
                mulher['0-9-m']+=1

            else:
                mulher['0-9-v']+=1


    #===========================================
    #   pergunta 2
    #  - qual a faixa etaria 10 a 19
        if coluna_faixa_etaria[i] == '10 a 19':
            mulher['10-19']+=1
    #   pergunta 3
    #   qtds obito sim
            if coluna_obito[i] == 'Sim':
                mulher['10-19-m']+=1
    #   pergunta 3
    #   qtds obito não
            else:
                mulher['10-19-v']+=1
        


#==============================================================
#               Homens
#==============================================================
print('''=========================================
        homen - 0 a 9
        total contabilizados={}

        total morto:{}
        total vivo:{}
'''.format(homen['0-9'],homen['0-9-m'],homen['0-9-v']))


print('''=========================================
        homen - 10 a 19
        total contabilizados={}

        total morto:{}
        total vivo:{}
'''.format(homen['10-19'],homen['10-19-m'],homen['10-19-v']))
#==============================================================
#               Mulher
#==============================================================
print('''=========================================
        mulher - 0 a 9
        total contabilizados={}

        total morto:{}
        total vivo:{}
'''.format(mulher['0-9'],mulher['0-9-m'],mulher['0-9-v']))


print('''=========================================
        mulher - 10 a 19
        total contabilizados={}

        total morto:{}
        total vivo:{}
'''.format(mulher['10-19'],mulher['10-19-m'],mulher['10-19-v']))
print('=========================================')
print(f'total contabilizados: {t}')
print('=========================================')
