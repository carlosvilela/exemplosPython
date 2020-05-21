#+-----------------------------------------------------------------+
#|                                        av2_questao02_letra_c.py |
#|                          Copyright 2020, Carlos Bezerra Vilela. |
#|                  https://github.com/carlosvilela/exemplosPython |
#+-----------------------------------------------------------------+

# valores de entrada
primeiroValor = 45
segundoValor = 5
primeiraLista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
segundaLista =  [0, 4, 8, 12, 16, 20, 24, 28, 32, 36]

# Função para somar dois valores
def somarDoisFatores (primeiraParcela, segundaParcela):
    soma = primeiraParcela + segundaParcela
    return soma


# Função para somar duas Listas
def somarDuasListas (primeiraLista, segundaLista):
    #Assumindo que ambas as listas têm o mesmo tamanho
    tamanhoLista = len(primeiraLista)
    resultado = []
    # rastrear lista, elemento por elemento
    for i in range(tamanhoLista):
        x = primeiraLista[i]
        y = segundaLista[i]
        resultado.append(x+y)
    return resultado

# Separador de calculo
print("==================================================================")

# Resultado da soma de dois valores
somarValore = somarDoisFatores(primeiroValor,segundoValor)
print(primeiroValor,"+",segundoValor,"= ",somarValore)

# Separador de calculo
print("==================================================================")

# Resultado da soma de duas listas
somarListas = somarDuasListas(primeiraLista,segundaLista)
print("Lista Parcela 1 -> ",primeiraLista)
print("Lista Parcela 2 -> ",segundaLista)
print("Resultado da Soma =", somarListas)

# Separador de calculo
print("==================================================================")
