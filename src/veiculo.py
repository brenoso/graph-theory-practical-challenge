import math
import datetime

class Veiculo:

    '''
    Construtor da classe
    '''
    def __init__(self, volume_maximo_suportado, valor_maximo_suportado, velocidade_inicial_final, velocidade_normal,
                        tempo_carga, tempo_descarga, custo_medio_hora, custo_medio_km, custo_fixo_diario, tipo_veiculo):

        # Variaveis de controle (backups)
        self._volume_maximo_suportado_inicial = volume_maximo_suportado
        self._valor_maximo_suportado_inicial = valor_maximo_suportado
        
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
        self._disponivel_para_trajeto = False # Após ser alocado para um centro, ficará disponível para entregas
        self._tempo_jornada_disponivel = 25200 # -> 7horas em segundos
        self._tipo_de_veiculo = tipo_veiculo
        self.localizacao_atual = None
        self.trajeto_feito = list()

        #controle de custos
        self._jornada_realizada = 0
        self._km_rodado = 0
        self._volume_carregado = 0
        self._custo_total_dia = 0
    
    # Sobrecarga da impressão do objeto
    def __str__(self):
        return "Veículo: " + self._tipo_de_veiculo + "\n\tCusto dia: " + str(self._custo_fixo_diario) + "\tCusto km: " + str(self._custo_medio_km) + "\tCusto hora: " + str(self._custo_medio_hora) + "\n\tVol. Máximo: " + str(self._volume_maximo_suportado) + "\tValor. Máximo: " + str(self._valor_maximo_suportado) + "\n\tVel. Ini/Fin: " + str(self._velocidade_inicial_final) + "\tVel. Normal: " + str(self._velocidade_normal)

    # Consideraremos que se restar somente 10% de tempo restante da jornada
    # disponivel, o veiculo será realocado para o centro
    def is_tempo_esgotado(self, centro):
        
        distancia_cliente_centro = centro.get_distancia_centro_ao_cliente(self.get_localizacao_atual().get_label())
        
        tempo_retorno_centro = (distancia_cliente_centro[0] / self._velocidade_inicial_final) * 120

        tempo_restante = self.get_tempo_jornada_disponivel() - tempo_retorno_centro

        if (tempo_restante > (25200 * 0.10)):
            return False

        return True

    # Deus abençoe esse código
    # Se o tempo de jornada for menor que o tempo de carregamento + o tempo de de trajeto até o cliente
    # setar o disponivel_para_trajeto como False.
    def is_trajeto_possivel(self, cliente, centro):

        check_volume = False
        check_tempo = False
        check_valor = False

        '''
        Calculos referentes a quantidade de pacotes
        '''
        quantidade_pacotes_para_entrega = 0

        volume_solicitado_cliente = cliente.get_volume_total()
        # Verifica se o veiculo é capaz de entregar todo o volume solicitado pelo cliente
        if ((self.get_volume_maximo_suportado() - volume_solicitado_cliente) > 0):
            check_volume = True
            quantidade_pacotes_para_entrega = cliente.get_qtd_pacotes_total()
        # Verifica se o veiculo é capaz de entregar alguma parte do volume solictado pelo cliente
        elif ((self.get_volume_maximo_suportado() // cliente.get_volumes_por_pacote()) > 0):
            check_volume = True
            quantidade_pacotes_para_entrega = self.get_volume_maximo_suportado() // cliente.get_volumes_por_pacote()
        else: 
            check_volume = False

        '''
        Calculos referentes ao valor da mercadoria
        '''
        if (quantidade_pacotes_para_entrega * cliente.get_preco_mercadoria_pacote() > 0):
            check_valor = True

        '''
        Calculos referentes ao tempo de viagem
        '''
        # Calcular a distancia do local atual do veiculo até o cliente
        distancia_veiculo_cliente = self.euclidian_distance(self.get_localizacao_atual().get_coordenadas(), cliente.get_coordenadas())

        # Calcular a distancia do cliente até o centro
        distancia_cliente_centro = self.euclidian_distance(cliente.get_coordenadas(), centro.get_coordenadas())

        # Pega a velocidade da localizacao atual do veiculo até o proximo cliente
        velocidade_localizacao_atual_cliente = 0
        if (self.get_localizacao_atual() is centro):
            velocidade_localizacao_atual_cliente = self.get_velocidade_inicial_final()
        else :
            velocidade_localizacao_atual_cliente = self.get_velocidade_normal()
        
        # Pega a velocidade do cliente até o centro
        velocidade_cliente_centro = self.get_velocidade_inicial_final()

        # Tempo de viagem em horas do ponto atual do veiculo até o cliente
        tempo_viagem_localizacao_atual_cliente = distancia_veiculo_cliente / velocidade_localizacao_atual_cliente
        # Transforma em segundos
        tempo_viagem_localizacao_atual_cliente *= 60 #converte para min
        tempo_viagem_localizacao_atual_cliente *= 60 #converte para seg

        # Tempo de viagem em horas do cliente até o centro
        tempo_viagem_cliente_centro = distancia_cliente_centro / velocidade_cliente_centro
        # Transforma em segundos
        tempo_viagem_cliente_centro *= 60 #converte para min
        tempo_viagem_cliente_centro *= 60 #converte para seg

        tempo_carga_segundos = self._tempo_carga
        tempo_carga_segundos *= 60 #converte para min
        tempo_carga_segundos *= 60 #converte para seg

        tempo_descarga_segundos = self._tempo_descarga
        tempo_descarga_segundos *= 60 #converte para min
        tempo_descarga_segundos *= 60 #converte para seg
        tempo_total_viagem = tempo_viagem_localizacao_atual_cliente + tempo_viagem_cliente_centro + (tempo_carga_segundos * quantidade_pacotes_para_entrega) + (tempo_descarga_segundos * quantidade_pacotes_para_entrega)
        
        if ((self._tempo_jornada_disponivel - round(tempo_total_viagem, 0)) > 0):
            check_tempo = True

        # Debita valores da entrega no cliente e no veiculo.
        if (check_tempo and check_valor and check_volume):
            #Debitos para validar viagem
            self._valor_maximo_suportado -= (quantidade_pacotes_para_entrega * cliente.get_preco_mercadoria_pacote())
            self._volume_maximo_suportado -= (quantidade_pacotes_para_entrega * cliente.get_volumes_por_pacote())
            self._tempo_jornada_disponivel -= round(tempo_total_viagem, 0)

            #Controle de custos
            self._km_rodado += distancia_veiculo_cliente
            self._jornada_realizada += round(tempo_total_viagem, 0)
            volume = quantidade_pacotes_para_entrega * cliente.get_volumes_por_pacote()
            self._volume_carregado += round(volume, 6)

            cliente.receber_volume(quantidade_pacotes_para_entrega, cliente.get_volumes_por_pacote())
            self.atualizar_localizacao_atual(cliente)

            return True

        return False

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
    
    def atualizar_localizacao_atual(self, local):
        self.localizacao_atual = local
        self.trajeto_feito.append(local)

    def is_disponivel_para_trajeto(self):
        return self._disponivel_para_trajeto

    def is_disponivel_para_alocacao(self):
        return self._disponivel_para_alocacao

    '''
    Altera os valores de volume máximo e valor máximo do veículo quando ele volta para o centro de distribuição, pois ele está vazio
    '''
    
    def reset_volume_maximo_suportado(self):
       self._volume_maximo_suportado = self.get_volume_maximo_suportado_inicial()

    def reset_valor_maximo_suportado(self):
       self._valor_maximo_suportado = self.get_valor_maximo_suportado_inicial()

    '''
    Conversão de dados e calculo de distância padrão
    '''
    def converte_segundos_em_tempo(self, tempo_para_conversao):
        horas = tempo_para_conversao // 3600

        segs_restantes = tempo_para_conversao % 3600
        minutos = segs_restantes // 60
        segs_restantes_final = segs_restantes % 60

        if (horas >= 24): 
            horas = int(horas % 24)
        
        return (str(int(horas)) + "h " + str(int(minutos)) + "m " + str(int(segs_restantes_final))+ "s")
    
    
    #TODO - Globalizar essa função
    def euclidian_distance(self, coordenadas_do_veiculo, coordenadas_do_vizinho):

        x1 = float(coordenadas_do_veiculo[0])
        y1 = float(coordenadas_do_veiculo[1])
        x2 = float(coordenadas_do_vizinho[0])
        y2 = float(coordenadas_do_vizinho[1])
        
        return math.sqrt((x2-x1)**2+(y2-y1)**2)
    
    
    '''
    Métodos getters e setters
    '''
    def get_localizacao_atual(self):
        return self.localizacao_atual

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
    
    def get_tempo_jornada_disponivel(self):
        return self._tempo_jornada_disponivel

    def get_tempo_jornada_realizada(self):
        return self._jornada_realizada
    
    def get_tipo_de_veiculo(self):
        return self._tipo_de_veiculo

    def get_volume_carregado(self):
        return self._volume_carregado

    def get_custo_por_dia(self):
        return self._custo_fixo_diario

    def get_custo_por_km(self):
        return self._custo_medio_km

    def get_custo_por_hora(self):
        return self._custo_medio_hora

    def get_volume_maximo_suportado_inicial(self):
        return self._volume_maximo_suportado_inicial

    def get_valor_maximo_suportado_inicial(self):
        return self._valor_maximo_suportado_inicial

    def get_trajeto_feito(self):
        return self.trajeto_feito

    def get_km_rodado(self):
        return self._km_rodado

    # Define para qual centro (região) o veículo será alocado
    def set_alocacao(self, centro):

        if (self.is_disponivel_para_alocacao()):
            self._centro_de_alocacao = centro.get_label()
            self._disponivel_para_alocacao = False
            self._disponivel_para_trajeto = True
            self.atualizar_localizacao_atual(centro)
        else:
            print("Erro ao alocar! Veiculo ja alocado!")

    def set_custo_total_dia(self, valor):
        self._custo_total_dia = valor