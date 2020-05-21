#+-----------------------------------------------------------------+
#|                                       av2_questao02_letra_ab.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

# valores de entrada
primeiroValor = 45
segundoValor = 5
primeiraLista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
segundaLista =  [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

# Função para subtrair dois valores
def subtrairDoisFatores (primeiraParcela, segundaParcela):
    soma = lambda a, b: (a+b)
    return soma (primeiraParcela,segundaParcela)

# Função para subtrair duas Listas
def subtrairDuasListas (primeiraParcela, segundaParcela):
    soma = list(map(lambda a,b: (a+b), primeiraParcela,segundaParcela))
    return soma


# Separador de calculo
print("==================================================================")

# Resultado da subtração de dois valores
diminuirValore = subtrairDoisFatores(primeiroValor,segundoValor)
print(primeiroValor,"+",segundoValor,"= ",diminuirValore)

# Separador de calculo
print("==================================================================")

# Resultado da subtração de duas listas
subtrairListas = subtrairDuasListas(primeiraLista,segundaLista)
print("Lista Parcela 1 -> ",primeiraLista)
print("Lista Parcela 2 -> ",segundaLista)
print("Resultado da Soma =", subtrairListas)

# Separador de calculo
print("==================================================================")
