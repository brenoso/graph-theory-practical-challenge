# -*- coding: utf-8 -*-

'''
Classe que representa um vértice do grafo (cliente)
'''
class Cliente:

    '''
    Construtor da classe
    '''
    def __init__(self, x, y, volume, preco_mercadoria, qtd_pacotes, regiao, label, qtd_vizinhos):

        # Variaveis referentes as mercadorias
        self._volume_total = volume
        self._preco_mercadoria_total = preco_mercadoria
        self._qtd_pacotes_total = qtd_pacotes

        self._volumes_por_pacote = 0#self._volume_total / self._qtd_pacotes_total
        self._preco_mercadoria_por_pacote = 0#self._preco_mercadoria_total / self._qtd_pacotes_total

        # Variaveis referentes a localizacao
        self._coordenada_x = x
        self._coordenada_y = y
        self._regiao = regiao
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

        volume_disponivel = self.get_volume_disponivel_para_entrega()

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
    def get_volume_disponivel_para_entrega(self):

        d = dict()
        d['volume_total_disponivel'] = self._volume_total
        d['volumes_por_pacote'] = self._volumes_por_pacote

        return d 

    def tem_demanda(self):
        return self._tem_demanda
    
    def get_regiao(self):
        return self._regiao

    def get_coordenada_x(self):
        return self._coordenada_x
    
    def get_coordenada_y(self):
        return self._coordenada_y
    
    def get_sendo_visitado(self):
        return self._sendo_visitado

    def get_preco_mercadoria_pacote(self):
        return self._preco_mercadoria_por_pacote

    def set_sendo_visitado(self):
        self._sendo_visitado = True

