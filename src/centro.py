from cliente import Cliente
from veiculo import Veiculo

class Centro:
    '''
    Construtor da classe
    '''
    def __init__(self, coordenadas, clientes, label):
        self._coordenadas = coordenadas
        self._clientes = clientes
        self._qtd_clientes = len(clientes)
        self._distancia_centro_ao_cliente = [None] * self._qtd_clientes  #Inicialmente a distancia para cada vertice é desconhecida
        self._volume_total = self._calcula_volume_total(clientes)
        self._label = label

        # Inicialmente sem nenhum veiculo, depois será feita uma heurística a partir da demanda de cada
        # centro e sera efetuada a distribuicao mais precisa possivel dos veiculos para cada centro
        self._veiculos = None
    
    def __str__(self):
        return "Centro: " + str(self._label) + "\t Qtd de Cliente: " + str(self._qtd_clientes) + "\t Volume Total: " + str(self._volume_total) 
        
    def _calcula_volume_total(self, clientes):
        
        somatorio_volume_clientes = sum(cliente.get_volume_total() for cliente in clientes)
        
        return somatorio_volume_clientes

    def adicionar_veiculos(self, veiculos):
        self._veiculos = veiculos

    '''
    Getters e Setters
    '''

    def set_distancia_centro_cliente(self, posicao, distancia):
        self._distancia_centro_ao_cliente.pop(posicao)
        self._distancia_centro_ao_cliente.insert(posicao, distancia)
    
    def get_coordenada(self):
        return self._coordenadas

    def get_quantidade_clientes(self):
        return self._qtd_clientes
    
    def get_volume_total(self):
        return self._volume_total