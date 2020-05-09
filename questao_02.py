#+-----------------------------------------------------------------+
#|                                                   questao_01.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

# valores de entrada
primeiroValor = 15
segundoValor = 5
primeiraLista = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
segundaLista =  [5, 10, 10, 15, 15, 15, 30, 35, 45, 15]

# Função para subtrair dois valores
def subtrairDoisFatores (minuendo, subtraendo):
    diferenca = lambda a, b: (a-b)
    return diferenca (minuendo,subtraendo)

# Função para subtrair duas Listas
def subtrairDuasListas (listaMinuendo, listaSubtraendo):
    diferenca = list(map(lambda a,b: (a-b), listaMinuendo,listaSubtraendo))
    return diferenca


# Separador de calculo
print("==================================================================")

# Resultado da subtração de dois valores
diminuirValore = subtrairDoisFatores(primeiroValor,segundoValor)
print(primeiroValor,"-",segundoValor,"= ",diminuirValore)

# Separador de calculo
print("==================================================================")

# Resultado da subtração de duas listas
subtrairListas = subtrairDuasListas(primeiraLista,segundaLista)
print("Lista Minuendo ...-> ",primeiraLista)
print("Lista Subtraendo ->  ",segundaLista)
print("......... Resultado =", subtrairListas)

# Separador de calculo
print("==================================================================")
