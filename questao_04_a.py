#+-----------------------------------------------------------------+
#|                                                   questao_01.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

# Entrada de dados
my_floats = [5.75, 8.09, 3.25, 20.55, 3.15, 8.08, 5.09]

# função para arredondar 2 casas decimais
def arredondarQuadradoValorEmDuasCasas (entradaDados):
    numeroCasaDecimal = 2
    arredondar = list (map(lambda x: round(x**2,numeroCasaDecimal), entradaDados))
    return arredondar

# Resultado
map_result = arredondarQuadradoValorEmDuasCasas(my_floats)

# imprimir valores
print(map_result)
