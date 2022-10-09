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
# Arquivo: listagem3\capítulo 11\11.28.py
##############################################################################

import sqlite3
from contextlib import closing

with sqlite3.connect("agenda.db") as conexão:
    with closing(conexão.cursor()) as cursor:
        cursor.execute("""delete from agenda
                                 where nome = 'Maria' """)
        print("Registros apagados: ", cursor.rowcount)
        if cursor.rowcount == 1:
            conexão.commit()
            print("Alterações gravadas")
        else:
            conexão.rollback()
            print("Alterações abortadas")
