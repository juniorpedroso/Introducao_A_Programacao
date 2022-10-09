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
# Arquivo: listagem3\capítulo 08\08.52.py
##############################################################################

while True:
    try:
        v = int(input("Digite um número inteiro (0 sai):"))
        if v == 0:
            break
    except Exception:
        print("Valor inválido! Redigite")
    else:
        print("Parabéns, nenhuma exceção")
    finally:
        print("Executado sempre, mesmo com break")
