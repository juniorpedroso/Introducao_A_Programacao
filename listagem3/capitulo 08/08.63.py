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
# Arquivo: listagem3\capítulo 08\08.63.py
##############################################################################

import types


def diz_o_tipo(a):
    if isinstance(a, str):
        return "String"
    elif isinstance(a, list):
        return "Lista"
    elif isinstance(a, dict):
        return "Dicionário"
    elif isinstance(a, int):
        return "Número inteiro"
    elif isinstance(a, float):
        return "Número decimal"
    elif isinstance(a, types.FunctionType):
        return "Função"
    elif isinstance(a, types.BuiltinFunctionType):
        return "Função interna"
    else:
        return str(type(a))


print(diz_o_tipo(10))
print(diz_o_tipo(10.5))
print(diz_o_tipo("Alô"))
print(diz_o_tipo([1, 2, 3]))
print(diz_o_tipo({"a": 1, "b": 50}))
print(diz_o_tipo(print))
print(diz_o_tipo(None))
