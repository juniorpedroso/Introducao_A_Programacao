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
# Arquivo: listagem3\capítulo 07\07.11.py
##############################################################################

s = "um tigre, dois tigres, três tigres"
s.find("tigres")
s.rfind("tigres")
s.find("tigres", 7)  # início=7
s.find("tigres", 30)  # início=30
s.find("tigres", 0, 10)  # início=0 fim=10
