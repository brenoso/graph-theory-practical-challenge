class Veiculo:
    '''
    Construtor da classe
    '''
    def __init__(self, volume, valor_maximo, velocidade_inicial_final, velocidade_normal, tempo_carga, tempo_descarga, custo_hora, custo_km, custo_fixo_diario):
        self._tipo_de_veiculo = self.set_tipo_veiculo(volume)
        self._volume = volume
        self._valor_maximo = valor_maximo
        self._velocidade_inicial_final = velocidade_inicial_final
        self._velocidade_normal = velocidade_normal
        self._tempo_carga = tempo_carga
        self._tempo_descarga = tempo_descarga
        self._custo_hora = custo_hora
        self._custo_km = custo_km
        self._custo_fixo_diario = custo_fixo_diario
        self._regiao_de_alocacao = None
        self._disponivel = True
        self._jornada_disponivel = 25200 # -> 7horas em segundos

    '''
    Define para qual região o veículo será alocado
    '''
    def set_alocacao(self, regiao):
         self._regiao_de_alocacao = regiao
         self._disponivel = False
    
    '''
    Debita tempo da jornada, para que o veículo não trabalhe mais que 7 horas
    '''
    def debita_jornada(self, tempo):
        self._jornada_disponivel = self._jornada_disponivel - tempo

    '''
    Define qual o tipo de véiculo de acordo com os valores fixados no arquivo
    gerador de instâncias para o trabalho
    '''
    def set_tipo_veiculo(self, volume):
        if(volume >= 8 and volume <= 16):
            tipo = "Van"
        elif(volume >= 2 and volume <= 4):
            tipo = "Mini-Van"
        elif(volume >= 0.7 and volume <= 1.4):
            tipo = "Comum"
        elif(volume >= 0.2 and volume <= 0.4):
            tipo = "Motocicleta"
        elif(volume >= 0.08 and volume <= 0.16):
            tipo = "Van terceirizada"
        else:
            tipo = "Erro na leitura"
        return tipo

    '''
    Métodos GET para os atributos da classe
    '''
    def get_volume(self):
        return self._volume

    def get_valor_maximo(self):
        return self._valor_maximo

    def get_velocidade(self, tipo = 'normal'):
        if(tipo == 'normal'):
            return self._velocidade_normal
        else:
            return self._velocidade_inicial_final

    def get_tempo(self, tipo = 'carga'):
        if(tipo == 'carga'):
            return self._tempo_carga
        else:
            return self._tempo_descarga

    def get_regiao(self):
        return self._regiao_de_alocacao

    def get_disponivel(self):
        return self._disponivel
    
    def get_jornada(self):
        return self._jornada_disponivel