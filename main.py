from matplotlib import pyplot as plt
import math

from src.reader import Reader
from src.centros import Centros
from src.cliente import Cliente

colors = ['blue', 'red', 'purple', 'pink', 'orange']
def euclidian_distance(x1, y1, x2, y2):
    return math.sqrt((x2-x1)**2+(y2-y1)**2)

reader = Reader()
lista_de_centros = list()
lista_de_clientes = list()

'''
Define as regiões de acordo com os dados do arquivo
Instancia os centros em uma lista de objetos
'''
coordenadas_sub_regioes = reader.get_coordenadas_sub_regioes()
x=0
for list in coordenadas_sub_regioes:
    #Lista com objetos do tipo Centros
    lista_de_centros.append(Centros(float(list[0]), float(list[1]), reader.get_qtd_clientes()))
    #Plota os pontos no plano
    plt.scatter(float(lista_de_centros[x].get_coordenada_x()),float(lista_de_centros[x].get_coordenada_y()), color='red')
    #Plota os "nomes" de cada centro, para facilitar a identificação
    plt.annotate(x, xy=(lista_de_centros[x].get_coordenada_x(),lista_de_centros[x].get_coordenada_y()), xytext=(5,-5), textcoords='offset points')
    x+=1
x=None

'''
Instancia os clientes em uma lista de objetos
'''
clientes = reader.get_clientes()
x=0
for list in clientes:
    #Lista com objetos do tipo Centros
    lista_de_clientes.append(Cliente(list[0], list[1], list[2], list[3], list[4], -1, x, len(clientes)))
    #Plota os pontos no plano
    plt.scatter(float(lista_de_clientes[x].get_coordenada_x()), float(lista_de_clientes[x].get_coordenada_y()), color='blue')
    #Plota os "nomes" de cada cenclientetro, para facilitar a identificação
    plt.annotate(x, xy=(float(lista_de_clientes[x].get_coordenada_x()), float(lista_de_clientes[x].get_coordenada_y())), xytext=(5,-5), textcoords='offset points')
    x+=1
x=None


'''
TODO = melhorar essa parte =D
Para cada centro é calculada a distância euclidiana dele até cada cliente
'''
contador_centro = contador_cliente = 0
for i in lista_de_centros:
    x1 = float(lista_de_centros[contador_centro].get_coordenada_x())
    y1 = float(lista_de_centros[contador_centro].get_coordenada_y())
    for j in lista_de_clientes:
        x2 = float(lista_de_clientes[contador_cliente].get_coordenada_x())
        y2 = float(lista_de_clientes[contador_cliente].get_coordenada_y())
        distancia_euclidiana = euclidian_distance(x1, y1, x2, y2)
        lista_de_centros[contador_centro].set_distacancia_centro_cliente(contador_cliente, distancia_euclidiana)
        contador_cliente+=1
    contador_centro+=1
    contador_cliente=0



'''
Desenha o plano cartesiano e imprime na tela
'''
#axis = Define os limites do plano. Nesse caso é definido como igual tanto para min,máx dos eixos X e Y.
plt.axis('equal')
#xlabel ou xlabel = Define o "nome" de cada eixo, nesse caso mantemos como X e Y
plt.xlabel("x")
plt.ylabel("y")
#show = exibe a plotagem dos pontos no plano cartesiano
plt.show()