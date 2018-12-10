class Veiculo:
    
    #Inicializa Classe Veículo
    def __init__(self, volume, valor_maximo, velocidade_inicial_final, velocidade_normal, tempo_carga, tempo_descarga, custo_hora, custo_km, custo_fixo_diario):
        self.__volume = volume
        self.__valor_maximo = valor_maximo
        self.__velocidade_inicial_final = velocidade_inicial_final
        self.__velocidade_normal = velocidade_normal
        self.__tempo_carga = tempo_carga
        self.__tempo_descarga = tempo_descarga
        self.__custo_hora = custo_hora
        self.__custo_km = custo_km
        self.__custo_fixo_diario = custo_fixo_diario
        self.__regiao_de_alocacao = None
        self.__disponivel = True
        self.__jornada_disponivel = 25200 # -> 7horas em segundos

    def setAlocacao(self, regiao):
         self.__regiao_de_alocacao = regiao
         self.__disponivel = False

    def debitaJornada(self, tempo):
        self.__jornada_disponivel = self.__jornada_disponivel - tempo

    
    '''
    Métodos GET para os atributos da classe
    '''
    def getVolume(self):
        return self.__volume

    def getValorMaximo(self):
        return self.__valor_maximo

    def getVelocidade(self, tipo = 'normal'):
        if(tipo = 'normal'):
            return self.__velocidade_normal
        else:
            return self.__velocidade_inicial_final

    def getTempo(self, tipo = 'carga'):
        if(tipo = 'carga'):
            return self.__tempo_carga
        else:
            return self.__tempo_descarga

    def getRegiao(self):
        return self.__regiao_de_alocacao

    def getDisponivel(self):
        return self.__disponivel
    
    def getJornada(self):
        return self.__jornada_disponivel
