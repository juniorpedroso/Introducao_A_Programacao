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
# Arquivo: listagem3\capítulo 05\05.12.py
##############################################################################

x = 1
soma = 0
while x <= 5:
    n = int(input(f"{x} Digite o número:"))
    soma = soma + n
    x = x + 1
print(f"Média: {soma / 5:5.2f}")
