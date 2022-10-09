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
# Arquivo: listagem3\capítulo 11\11.62.py
##############################################################################

create table tipos(id integer primary key autoincrement,
                   descrição text);
create table nomes(id integer primary key autoincrement,
                   nome text);
create table telefones(id integer primary key autoincrement,
                       id_nome integer, número text,
                       id_tipo integer);
