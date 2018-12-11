class Centros:
    '''
    Construtor da classe
    '''
    def __init__(self, x, y):
        self._coordenada_x = x
        self._coordenada_y = y
        self._quantidade_de_clientes = 0
        self._volume_total = 0

    def get_coordenada_x(self):
        return self._coordenada_x

    def get_coordenada_y(self):
        return self._coordenada_y

    def get_quantidade_clientes(self):
        return self._quantidade_de_clientes
    
    def get_volume_total(self):
        return self._volume_total