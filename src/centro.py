from cliente import Cliente
from veiculo import Veiculo
import math

class Centro:
    '''
    Construtor da classe
    '''
    def __init__(self, coordenadas, clientes, label):
        self._coordenadas = coordenadas
        self._clientes = clientes
        self._qtd_clientes = len(clientes)
        self._distancia_centro_ao_cliente = [] #Inicialmente a distancia para cada vertice é desconhecida
        self._volume_total = self._calcula_volume_total(clientes)
        self._valor_total_todos_clientes = self._calcula_valor_total_todos_clientes(clientes)
        self._label = label

        # Inicialmente sem nenhum veiculo, depois será feita uma heurística a partir da demanda de cada
        # centro e sera efetuada a distribuicao mais precisa possivel dos veiculos para cada centro
        self._veiculos = list()

        # No momento da incialização do Centro é calcula a distância dele para todos os seus clientes
        self.set_distancia_centro_todos_cliente()
    
    def __str__(self):
        return "Centro: " + str(self._label) + "\t Qtd de Cliente: " + str(self._qtd_clientes) + "\t Volume Total: " + str(self._volume_total) 
        
    def _calcula_volume_total(self, clientes):
        
        somatorio_volume_clientes = sum(cliente.get_volume_total() for cliente in clientes)
        
        return somatorio_volume_clientes

    def _calcula_valor_total_todos_clientes(self, clientes):
        
        somatorio_valor_total_clientes = sum(cliente.get_valor_total() for cliente in clientes)
        
        return somatorio_valor_total_clientes

    def set_veiculo(self, veiculo):
        self._veiculos.append(veiculo)

    '''
    Getters e Setters
    '''
    def get_coordenada(self):
        return self._coordenadas

    def get_quantidade_clientes(self):
        return self._qtd_clientes
    
    def get_volume_total(self):
        return self._volume_total

    def get_valor_total_todos_clientes(self):
        return self._valor_total_todos_clientes

    def get_label(self):
        return self._label

    def get_distancia_centro_ao_cliente(self, label_cliente):
        #Buscará qual é a sub-lista que se encontra o valor "label_cliente", armazenando esta sub-lista em x. 
        #O valor retornado será (x[1]), onde x[1] corresponde ao campo da distância do cliente até o centro
        return [(x[1]) for x in self._distancia_centro_ao_cliente if label_cliente in x]

    #Define a distância do cliente para todos os demais da sua região
    def set_distancia_centro_todos_cliente(self):
        linha = []
        #Para cada cliente na sua lista de clientes, calcula a distância entre os pontos
        for cliente in self._clientes:
            #Cria uma "linha" na matriz 2D, no qual a posição 0 trata-se do ID do vizinho e a posição da distância para esse vizinho
            linha = [cliente.get_label(), self.euclidian_distance(self._coordenadas, cliente.get_coordenadas())]
            #Cada "linha" em uma posição do atributo para facilitar a busca
            self._distancia_centro_ao_cliente.append(linha)

    def euclidian_distance(self, coordenadas_do_vertice, coordenadas_do_vizinho):
        x1 = float(coordenadas_do_vertice[0])
        y1 = float(coordenadas_do_vertice[1])
        x2 = float(coordenadas_do_vizinho[0])
        y2 = float(coordenadas_do_vizinho[1])
        return math.sqrt((x2-x1)**2+(y2-y1)**2)

    def imprime_veiculos_alocados(self):
        resultado = "Centro " + str(self._label) + ". Total de Veículos: " + str(len(self._veiculos)) + "\n"
        for veiculo in self._veiculos:
            resultado = resultado + "\tVeículo: " + str(veiculo.get_tipo_de_veiculo()) + "\t\tJornada Disponível: " + str(veiculo.converte_segundos_em_tempo()) + "\tVolume em Carga: " + str(veiculo.get_volume_em_carregamento()) + "\n"
        resultado = resultado + "\n\n"
        return resultado
