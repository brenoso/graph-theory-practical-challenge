from matplotlib import pyplot as plt

from src.reader import Reader
from src.centros import Centros
from src.cliente import Cliente

reader = Reader()
lista_de_centros = list()
lista_de_clientes = list()


clientes = reader.get_clientes()
x=0
for list in clientes:
    #Lista com objetos do tipo Centros
    lista_de_clientes.append(Cliente(list[0], list[1], list[2], list[3], list[4], -1, -1, len(clientes)))
    #Plota os pontos no plano
    plt.scatter(float(lista_de_clientes[x].get_coordernada_x()), float(lista_de_clientes[x].get_coordernada_y()), color='blue')
    x+=1
x=None

'''
Define as regiões de acordo com os dados do arquivo
'''

coordenadas_sub_regioes = reader.get_coordenadas_sub_regioes()
x=0
for list in coordenadas_sub_regioes:
    #Lista com objetos do tipo Centros
    lista_de_centros.append(Centros(list[0], list[1]))
    #Plota os pontos no plano
    plt.scatter(float(lista_de_centros[x].get_coordenada_x()),float(lista_de_centros[x].get_coordenada_y()), color='red')
    #Plota os "nomes" de cada centro, para facilitar a identificação
    plt.annotate(x, xy=(lista_de_centros[x].get_coordenada_x(),lista_de_centros[x].get_coordenada_y()), xytext=(5,-5), textcoords='offset points')
    x+=1
x=None


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