#+-----------------------------------------------------------------+
#|                                                 av2_questa05.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

# Bibliotecas
from functools import reduce

# Entrada de dados
my_floats = [4.35, 6.09, 3.25, 9.77, 2.16, 8.88, 4.59]

# função para arredondar valores de uma lista
def arredondarLista(entrada, casasDecimais):
    resultado = list (map(lambda x: round(x,casasDecimais), entrada))
    return resultado

# função para calcular o quadrado do valor em uma lista
def quadradoValor (entradaDados):
    arredondar = list (map(lambda x: x**2, entradaDados))
    return arredondar

# função condicional, separar valores menores ou iguais a 20
def valoresMenoresQue (valorVerificador):
    valorComparacao = 20
    return valorVerificador<=valorComparacao

# função para somar duas parcelas
def somarValores(primeiraParcela, segundaParcela):
    return primeiraParcela + segundaParcela

# Arredondar o quadrado do valor da lista em 3 casas
calcularQuadradoValor = quadradoValor(my_floats)
map_result = arredondarLista(calcularQuadradoValor,3)

# separar valores da lista, todos os menores ou iguais a 20
filter_result = list (filter(valoresMenoresQue, map_result))

# Somar os valores da lista e arredondar em 3 casas
calcularSomarLista = reduce(somarValores, filter_result)
reduce_result = round(calcularSomarLista,3)

# imprimir valores
print("my_floats ....= ",my_floats)
print("map_result ...= ",map_result)
print("filter_result = ",filter_result)
print("reduce_result = ",reduce_result)
