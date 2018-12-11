class Centros:
    '''
    Construtor da classe
    '''
    def __init__(self, x, y, qtd_clientes):
        self._coordenada_x = x
        self._coordenada_y = y
        self._quantidade_de_clientes = 0
        
        self._distancia_centro_ao_cliente = [None] * qtd_clientes  #Inicialmente a distancia para cada vertice é desconhecida
        self._volume_total = 0
    
    def set_distacancia_centro_cliente(self, posicao, distancia):
        self._distancia_centro_ao_cliente.pop(posicao)
        self._distancia_centro_ao_cliente.insert(posicao, distancia)
    
    def get_coordenada_x(self):
        return self._coordenada_x

    def get_coordenada_y(self):
        return self._coordenada_y

    def get_quantidade_clientes(self):
        return self._quantidade_de_clientes
    
    def get_volume_total(self):
        return self._volume_total