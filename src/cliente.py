# -*- coding: utf-8 -*-

'''
Classe que representa um vértice do grafo (cliente)
'''
class Cliente:

    '''
    Construtor da classe
    '''
    def __init__(self, coordenadas, volume, preco_mercadoria, qtd_pacotes, centro, label, qtd_vizinhos):

        # Variaveis referentes as mercadorias
        self._volume_total = volume
        self._preco_mercadoria_total = preco_mercadoria
        self._qtd_pacotes_total = qtd_pacotes

        self._volumes_por_pacote = self._volume_total / self._qtd_pacotes_total
        self._preco_mercadoria_por_pacote = self._preco_mercadoria_total / self._qtd_pacotes_total

        # Variaveis referentes a localizacao
        self._coordenadas = coordenadas
        self._centro = centro
        self._sendo_visitado = False
        self._tem_demanda = True

        # Variaveis referente aos objetos
        self._label = label
        self._distancia_vertices = [None] * qtd_vizinhos  #Inicialmente a distancia para cada vertice é desconhecida

    '''
    É esperado que o veiculo consulte a quantidade de volume total
    e a quantidade de volumes por pacote, e envie uma quantidade de volume
    multipla da quantidade de volume por pacote de cada cliente para garantir
    que sempre será debitado um numero inteiro de pacotes
    '''
    def receber_volume(self, volume_recebido):

        volume_disponivel = self.get_volume_total()

        if (volume_recebido <= volume_disponivel):
            self._volume_total = self._volume_total - volume_recebido
            self._qtd_pacotes_total = self._qtd_pacotes_total - (volume_recebido / self._volumes_por_pacote)
        else:
            print("O volume recebido ultrapassa o volume restante do cliente!")

        if (self._volume_total == 0):
            self._tem_demanda = False
    
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

    def get_volume_total(self):
        return self._volume_total

    def tem_demanda(self):
        return self._tem_demanda
    
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
    
    def get_volume(self):
        return self._volume_total

    def set_sendo_visitado(self):
        self._sendo_visitado = True

