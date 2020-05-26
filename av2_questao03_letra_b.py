# Bibliotecas
import numpy
import matplotlib.pyplot as plt

# Entrada de Dados - Eixo X - Dias em que houveram as apurações
dias_apurados = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31, # 01/março/2020 a 31/março/2020
                 32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57] # 01/abril/2020 a 26/abril/2020
x = dias_apurados

# Entrada de Dados - Euxo Y - Casos Apurados diários
casos_acumulados=[0,0,0,0,1,1,2,3,3,8,13,16,16,22,24,31,33,45,65,109,119,186,233,305,370,421,493,558,600,657,708,# 01/março/2020 a 31/março/2020
                  832,992,1074,1246,1394,1461,1688,1938,2216,2464,2607,2855,3231,3410,3743,3944,4349,4543,4765,4899,5306,5552,6172,6282,None,7111]# 01/abril/2020 a 26/abril/2020
y = casos_acumulados


# Pesquisa o indice da lista que contem o valor da pesquisa
def pesquisarLista (entradaLista, valorPesquisa):
    tamanhoLista = len(entradaLista)
    flag = -1
    for i in range(tamanhoLista):
        if (entradaLista[i] == valorPesquisa):
            flag = i
    return flag

def gerarListaAte (entradaLista, valorParada):
    tamanhoLista = len(entradaLista)
    novaLista = []
    for i in range(tamanhoLista):
        novaLista.append(entradaLista[i])
        if (entradaLista[i] == valorParada):
            del(novaLista[i])
            break
    return novaLista


# Estima o priximo valor da Lista
def estimarProximoValor (entradaListaX,entradaListaY):
    x = []
    y = []
    x = entradaListaX
    y = entradaListaY
    tamanhoLista = len(entradaListaY)
    x_estimado = tamanhoLista

    # Modelo polinomial baseado em equação do terceiro grau
    coeficiente = numpy.polyfit(x, y, 3)  # Polinomio terceiro grau
    mymodel = numpy.poly1d(coeficiente)
    print("===============================================================================================================")
    print("Modelo polinomial da estimativa do elemento faltante")
    print(mymodel)  # Imprimir modelo polinomial

    # Realizar calculos com o modelo polinomial
    calculo = ((coeficiente[0]*pow(x_estimado, 3)) + (coeficiente[1]*pow(x_estimado, 2)) + (coeficiente[2]*pow(x_estimado, 1)) + coeficiente[3])
    return calculo


indiceLista = pesquisarLista(casos_acumulados,None)
listaX = gerarListaAte(dias_apurados,dias_apurados[indiceLista])
listaY = gerarListaAte(casos_acumulados,casos_acumulados[indiceLista])
valorEstimado = round(estimarProximoValor(listaX,listaY),0)
print("===============================================================================================================")
print("casos_acumulados[",indiceLista,"] = ",casos_acumulados[indiceLista])
print("casos_acumulados[",indiceLista,"] = estimativa de ",valorEstimado)
print("===============================================================================================================")

# alterar o valor perdido e colocar o valor estimado
y [indiceLista] = valorEstimado

# inserir o dia de apuração para calcular a estimativa de casos acumulados
x_estimado = 58 # referente ao dia 27/abril/2020

# Modelo polinomial baseado em equação do terceiro grau
coeficiente = numpy.polyfit(x, y, 3) # Polinomio terceiro grau
mymodel = numpy.poly1d(coeficiente)
print("Modelo polinomial geral dos casos acumulados incluindo a estimativa do elemento faltante")
print(mymodel) # Imprimir modelo polinomial
print("===============================================================================================================")

# Realizar calculos com o modelo polinomial
calculo = ((coeficiente[0]*pow(x_estimado, 3)) + (coeficiente[1]*pow(x_estimado, 2)) + (coeficiente[2]*pow(x_estimado, 1)) + coeficiente[3])

# String apresentando a estimatia
texto = "Estimativa 27/04/2020: ", round(calculo,0)
texto1 = "Estimativa 25/04/2020: ", round(valorEstimado,0)

print(texto) #Imprimir resultado do calculo

# Gerar Gráfico
myline = numpy.linspace(1, x_estimado, 100)
plt.scatter(x, y)
plt.plot(myline, mymodel(myline))
plt.legend([texto, texto1]) # mostrar estimativa no grafico
print("===============================================================================================================")
plt.show()
