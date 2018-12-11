class Centro:
    '''
    Construtor da classe
    '''
    def __init__(self, coordenadas, qtd_clientes):
        self._coodernadas = coordenadas
        self._quantidade_de_clientes = 0
        
        self._distancia_centro_ao_cliente = [None] * qtd_clientes  #Inicialmente a distancia para cada vertice é desconhecida
        self._volume_total = 0
    
    def set_distacancia_centro_cliente(self, posicao, distancia):
        self._distancia_centro_ao_cliente.pop(posicao)
        self._distancia_centro_ao_cliente.insert(posicao, distancia)
    
    def get_coordenada(self):
        return self._coordenadas

    def get_quantidade_clientes(self):
        return self._quantidade_de_clientes
    
    def get_volume_total(self):
        return self._volume_total