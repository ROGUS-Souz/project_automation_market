import pyautogui as py
import time

py.PAUSE = 1
time.sleep(2)
# Lógica de Programação

def abrir(): # Função Abrir
    py.leftClick(x=866, y=989) # Clicar em adicionar
    time.sleep(5) # Esperar 5 segundos
    py.leftClick(x=1077, y=317) # Clicar em descrição
    if a == 'Folha':
        py.write(f'{a} - Proteina') # Escrever a descrição
    elif a == 'Obra':
        py.write(f'{a} - Proteina')
    elif a == 'Evento':
        py.write(f'{a} - Proteina')
    elif a == 'Equipe':
        py.write(f'{a} - Proteina')


def centro_de_custo(): # Função centro de custo
    py.leftClick(x=721, y=524) # clicar no centro de custo
    if a == 'Folha': # escrever o centro de custo + clicar no centro de custo 2
        py.write(f'CENTRO DE CUSTO - {a}')
    elif a == 'Obra':
        py.write(f'CENTRO DE CUSTO - {a}')
    elif a == 'Evento':
        py.write(f'CENTRO DE CUSTO - {a}')
    elif a == 'Equipe':
        py.write(f'CENTRO DE CUSTO - {a}')
    time.sleep(3)
    py.click(x=871, y=524,clicks=2)
    py.leftClick(x=905, y=558)
    py.leftClick(x=1875, y=990) # clicar em salvar
    time.sleep(5) # esperar 5 segundos
    py.press('enter') # apertar enteder
    
# Função add produto
def add_produto():
    contador = 0
    while contador < (len(proteinas)+1):    
        nome, quantidade = next(itens)  # Pega o próximo item
        if contador == 0:
            py.leftClick(x=882, y=987) # clicar em adicionar PRECISA ALTERAR - TEM UM CLIQUE DIFERENTE EM ADD - O BOTÃO VAI P O LADO
        else:
            py.leftClick(x=952, y=993)
        py.leftClick(x=1223, y=316) # clicar em produto
        py.write(nome) # escrever o nome do produto a ser lançado
        time.sleep(2) # esperar 5 segundos
        py.leftClick(x=1213, y=349) # clicar no nome do produto
        py.leftClick(x=804, y=390) # clicar na quantidade
        py.write(f'{quantidade}')# escrever a quantidade
        py.leftClick(x=1873, y=987)# clicar em salvar
        time.sleep(2)# esperar 5 segundos
        contador +=1

# Lista de produtos a serem lançados
proteinas = { #BOVINOS
             'bucho bovino - kg (estoque)':0,'alcatra com maminha - kg (estoque)':0,'mocoto bovino - kg (estoque)':0,'lagarto bovino - kg (estoque)':0,
             'paleta bovina sem musculo - kg (estoque)':20, 'coxao mole bovino - kg (estoque)':0,'almondega bovina -kg - (estoque)':20,
             #EMBUTIDOS
             'Salsicha hot dog kg (estoque)':0,
             #SUINOS
             'bacon manta kg (estoque)':0, 'costelinha suina - kg (estoque)':0, 'copa lombo (estoque)':20,'linguica calabresa - kg - estoque':10,
             'linguica suina toscana kg (estoque)':0,'picanha suina - kg - (estoque)':0,'linguica fina mista (estoque)':0,'pernil s/osso 1kg (estoque)':20,             
             #AVES
             'file de peito de frango (estoque)':60,'coxa/sobrecoxa desossada (estoque)':0,'coxa e sobrecoxa com osso kg':0,       
             #PESCADOS 
             'file de panga (estoque)': 0,'file de tilapia (estoque)':0,'file de polaca kg (estoque)':0,            
            }
itens = iter(proteinas.items())  # Transforma em iterador

a = 'Evento'
abrir()
centro_de_custo()
add_produto()

# b = py.position()
# print(b)

# c = len(proteinas)
# print(c)

# PRTOTEINAS ZERADAS

# # proteinas = { #BOVINOS
#                'bucho bovino - kg (estoque)':0,'alcatra com maminha - kg (estoque)':0,'mocoto bovino - kg (estoque)':0,'lagarto bovino - kg (estoque)':0,
#                'paleta bovina sem musculo - kg (estoque)':0, 'coxao mole bovino - kg (estoque)':0,'almondega bovina -kg - (estoque)':0,
#                #EMBUTIDOS
#                'Salsicha hot dog kg (estoque)':0,
#                #SUINOS
#                'bacon manta kg (estoque)':0, 'costelinha suina - kg (estoque)':0, 'copa lombo (estoque)':0,'linguica calabresa - kg - estoque':0,
#                'linguica suina toscana kg (estoque)':0,'picanha suina - kg - (estoque)':0,'linguica fina mista (estoque)':0,             
#                #AVES
#                'file de peito de frango (estoque)':0,'coxa/sobrecoxa desossada (estoque)':0,'coxa e sobrecoxa com osso kg':0,       
#                #PESCADOS 
#                'file de panga (estoque)': 0,'file de tilapia (estoque)':0,'file de polaca kg (estoque)':0,            
# #             }