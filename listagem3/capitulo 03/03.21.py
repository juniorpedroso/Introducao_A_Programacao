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
# Arquivo: listagem3\capítulo 03\03.21.py
##############################################################################

nome = "João"
idade = 22
grana = 51.34
f"{nome} tem {idade} anos e R${grana} no bolso."
f"{nome:12} tem {idade:3} anos e R${grana:5.2f} no bolso."
f"{nome:12} tem {idade:03} anos e R${grana:5.2f} no bolso."
f"{nome:<12s} tem {idade:<3} anos e R${grana:5.2f} no bolso."
