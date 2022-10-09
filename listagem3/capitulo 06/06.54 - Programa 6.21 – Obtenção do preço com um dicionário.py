##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2020
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Terceira Edição - Janeiro/2019 - ISBN 978-85-7522-718-3
#
# Site: https://python.nilo.pro.br/
#
# Arquivo: listagem3\capítulo 06\06.54 - Programa 6.21 – Obtenção do preço com um dicionário.py
##############################################################################

# Programa 6.21 – Obtenção do preço com um dicionário
tabela = {"Alface": 0.45,
          "Batata": 1.20,
          "Tomate": 2.30,
          "Feijão": 1.50}
while True:
    produto = input("Digite o nome do produto, fim para terminar:")
    if produto == "fim":
        break
    if produto in tabela:
        print(f"Preço {tabela[produto]:5.2f}")
    else:
        print("Produto não encontrado!")
