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
# Arquivo: listagem3\capítulo 08\08.79.py
##############################################################################

def gerador_de_numeros():
    i = 0
    while True:
        yield i
        i += 1


g = gerador_de_numeros()
g
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
next(g)
