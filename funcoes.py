# Funções
# input()
# len()
# split()
# Oque elas tem em comum?

'''def nome_da_funcao(parametros):
       comandos 
'''

# def dar_boas_vindas():
#     print('Bem-Vindo')

# dar_boas_vindas()

# def dar_boas_vindas_personalizada(nome):
#     print(f'Bem-Vindo(a) {nome}')

# dar_boas_vindas_personalizada("Márcio")


# def apresentar_lugar(horario_de_funcionamento, lugar = 'nossa loja'):
#     print(f'Conheça {lugar}, horário de funcionamento das {horario_de_funcionamento}')


# apresentar_lugar("08:00 às 18:00", "Disney")


#desafio 1
## Crie uma função chamada gerar_nome_completo que recebe como parâmetro o nome e sobrenome de alguém e dá boas vindas para essa pessoa

# def gerar_nome_completo(nome, sobrenome):
#     print(f'Seja bem-vindo(a) {nome} {sobrenome}')

# gerar_nome_completo('Márcio','Silva')

#desafio2
## Crie uma função chamada calcular_valores que recebe 2 parâmetros o primeiro o preço de um produto eo segundoparametro é a quantidade,
##porem a quantidade deve haver um valor padrao de 1. Sua funçao deve exibir o resultado do preço do produto, multiplicado a quantidade escolhida.

def calcular_valores(preco,quantidade = 1):
    resultado = float(preco) * int(quantidade)
    print(f'o resultado é: {resultado}')

calcular_valores(10,2)
