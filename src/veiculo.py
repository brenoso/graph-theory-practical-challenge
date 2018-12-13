class Veiculo:

    '''
    Construtor da classe
    '''
    def __init__(self, volume_maximo_suportado, valor_maximo_suportado, velocidade_inicial_final, velocidade_normal,
                        tempo_carga, tempo_descarga, custo_medio_hora, custo_medio_km, custo_fixo_diario, tipo_veiculo):

        # Variaveis explicitas no arquivo
        self._volume_maximo_suportado = volume_maximo_suportado # volume máximo (em m3) que o veículo pode transportar
        self._valor_maximo_suportado = valor_maximo_suportado # valor máximo (em reais) que o veículo pode transportar
        self._velocidade_inicial_final = velocidade_inicial_final # velocidade a qual o veículo se move entre o centro de distribuição e a primeira entrega, assim como entre a última entrega e o centro de distribuição
        self._velocidade_normal = velocidade_normal # velocidade com a qual o veículo se move entre duas entregas
        self._tempo_carga = tempo_carga # tempo médio para se carregar um pacote no veículo
        self._tempo_descarga = tempo_descarga # tempo médio necessário para descarregar um pacote do veículo e entregá-lo ao cliente
        self._custo_medio_hora = custo_medio_hora # custo médio por hora do veículo
        self._custo_medio_km = custo_medio_km # custo médio por quilômetro percorrido pelo veículo
        self._custo_fixo_diario = custo_fixo_diario # custo fixo diário do veículo
        
        ## Variaveis elucidadas ##

        # Variaveis a respeito da alocacao ao centro de distribuicao
        self._centro_de_alocacao = None
        self._disponivel_para_alocacao = True

        # Outras
        self._volume_carregado = 0 # Volume especifico carregado no veiculo para cada trajeto
        self._disponivel_para_trajeto = False # Após ser alocado para um centro, ficará disponível para entregas
        self._tempo_jornada_disponivel = 25200 # -> 7horas em segundos
        self._tipo_de_veiculo = tipo_veiculo
    
    def __str__(self):
        return "Veículo: " + self._tipo_de_veiculo + "\tDisponível: " + str(self._disponivel_para_alocacao) + "\tVolume Carregado: " + str(self._volume_carregado)

    '''
    Debita tempo da jornada, para que o veículo não trabalhe mais que 7 horas
    '''
    def debita_tempo_jornada(self, tempo):
        self._tempo_jornada_disponivel = self._tempo_jornada_disponivel - tempo

    '''
    Efetua todas as acoes necessárias para um trajeto, como debitar o tempo de jornada,
    mudança de status das variáveis, etc
    '''
    def inicia_trajeto(self):
        return False

    '''
    Métodos getters e setters
    '''

    # Define para qual centro (região) o veículo será alocado
    def set_alocacao(self, centro):

        if (self.is_disponivel_para_alocacao()):
            self._centro_de_alocacao = centro
            self._disponivel_para_alocacao = False
            self._disponivel_para_trajeto = True
        else:
            print("Erro ao alocar! Veiculo ja alocado!")
        
    def get_volume_maximo_suportado(self):
        return self._volume_maximo_suportado

    def get_valor_maximo_suportado(self):
        return self._valor_maximo_suportado

    def get_velocidade_normal(self):
        return self._velocidade_normal
    
    def get_velocidade_inicial_final(self):
        return self._velocidade_inicial_final

    def get_tempo_carga(self):
        return self._tempo_carga
    
    def get_tempo_descarga(self):
        return self._tempo_descarga

    def get_centro(self):
        return self._centro_de_alocacao

    def is_disponivel_para_alocacao(self):
        return self._disponivel_para_alocacao
    
    def get_tempo_jornada_disponivel(self):
        return self._tempo_jornada_disponivel
    
    def get_tipo_de_veiculo(self):
        return self._tipo_de_veiculo