import math


'''
Classe que representa um vértice do grafo (cliente)
'''
class Cliente:

    '''
    Construtor da classe
    '''
    def __init__(self, coordenadas, volume, preco_mercadoria, qtd_pacotes, centro, label):

        # Variaveis referentes as mercadorias
        self._volume_total = round(volume, 8)
        self._preco_mercadoria_total = preco_mercadoria
        self._qtd_pacotes_total = round(qtd_pacotes, 8)

        self._volumes_por_pacote = self._volume_total / self._qtd_pacotes_total
        self._preco_mercadoria_por_pacote = self._preco_mercadoria_total / self._qtd_pacotes_total

        # Variaveis referentes a localizacao
        self._coordenadas = coordenadas
        self._centro = centro
        self._sendo_visitado = False
        self._tem_demanda = True

        # Variaveis referente aos objetos
        self._label = label
        self._distancia_vertices = [] #Inicialmente a distancia para cada vertice é desconhecida
    
    # Sobrecarga da impressão do objeto
    def __str__(self):
        return "Cliente: " + str(self._label) + "\t Centro de Atendimento: " + str(self._centro) + "\t Volume Pedido: " + str(self._volume_total) + "\t Qtd Pacotes: " + str(self._qtd_pacotes_total)

    '''
    É esperado que o veiculo consulte a quantidade de volume total
    e a quantidade de volumes por pacote, e envie uma quantidade de volume
    multipla da quantidade de volume por pacote de cada cliente para garantir
    que sempre será debitado um numero inteiro de pacotes
    '''
    def receber_volume(self, volume_recebido):

        volume_disponivel = round(self.get_volume_total(), 8)
        volume_disponivel = round(volume_disponivel, 8)

        volume_recebido = round(volume_recebido, 8)

        if (volume_recebido <= volume_disponivel):
            self._volume_total = self._volume_total - volume_recebido
            self._qtd_pacotes_total = self._qtd_pacotes_total - (volume_recebido / self._volumes_por_pacote)
        else:
            print("O volume recebido ultrapassa o volume restante do cliente!")

        if (self._volume_total == 0):
            self._tem_demanda = False
    
    def tem_demanda(self):
        return self._tem_demanda

    #TODO - Globalizar essa função
    def euclidian_distance(self, coordenadas_do_vertice, coordenadas_do_vizinho):

        x1 = float(coordenadas_do_vertice[0])
        y1 = float(coordenadas_do_vertice[1])
        x2 = float(coordenadas_do_vizinho[0])
        y2 = float(coordenadas_do_vizinho[1])
        
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    '''
    Getters e Setters
    '''

    '''
    Será retornado o volume total disponivel para entrega
    e a quantidade de volumes por pacotes. Caso nao seja possivel
    o veiculo entregar o total de volume disponivel, ele entregara um valor multiplo
    do volume por pacote desse cliente, que representara um numero inteiro de pacotes
    '''
    def get_volumes_disponiveis_para_entrega(self):

        d = dict()
        d['volume_total_disponivel'] = self._volume_total
        d['volumes_por_pacote'] = self._volumes_por_pacote

        return d

    def get_distancias_vizinhos(self):
        return self._distancia_vertices
    
    def get_volumes_por_pacote(self):
        return self._volumes_por_pacote

    def get_volume_total(self):
        return self._volume_total
    
    def get_valor_total(self):
        return self._preco_mercadoria_total
    
    def get_centro(self):
        return self._centro

    def get_coordenadas(self):
        return self._coordenadas
    
    def get_sendo_visitado(self):
        return self._sendo_visitado

    def get_preco_mercadoria_pacote(self):
        return self._preco_mercadoria_por_pacote

    def get_label(self):
        return self._label

    def get_qtd_pacotes_total(self):
        return self._qtd_pacotes_total

    def get_distancia_ao_vizinho(self, label_vizinho):
        #Buscará qual é a sub-lista que se encontra o valor "label_vizinho", armazenando esta sub-lista em x. 
        #O valor retornado será (x[1]), onde x[1] corresponde ao campo da distância do cliente até o seu vizinho de região
        return [(x[1]) for x in self._distancia_vertices if label_vizinho in x]

    def set_sendo_visitado(self):
        self._sendo_visitado = True

    #Define a distância do cliente para todos os demais da sua região
    def set_distancia_para_vizinhos(self, lista_de_vizinhos):
        linha = []
        #Para cada vizinho da sua lista de vizinhos da região
        for vizinho in lista_de_vizinhos:
            #Cria uma "linha" na matriz 2D, no qual a posição 0 trata-se do ID do vizinho e a posição da distância para esse vizinho
            linha = [vizinho.get_label(), self.euclidian_distance(self._coordenadas, vizinho.get_coordenadas())]
            #Cada "linha" em uma posição do atributo para facilitar a busca
            self._distancia_vertices.append(linha)