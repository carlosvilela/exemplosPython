#+-----------------------------------------------------------------+
#|                                                   questao_01.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

# Entrada de dados
my_floats = [5.75, 8.09, 3.25, 20.55, 3.15, 8.08, 5.09]

# função condicional
def valoresMenoresQue (valorVerificador):
    return valorVerificador<=10

map_result = list (filter(valoresMenoresQue, my_floats))

# imprimir valores
print(map_result)
