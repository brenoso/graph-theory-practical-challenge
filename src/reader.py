import os
import sys

class Reader(object):

    '''
    Construtor da classe
    '''
    def __init__(self):
        self.__path = self._get_arquivo_path()
        self.__arquivo = self._ler_arquivo(self.__path)

    '''
    Efetua a leitura no arquivo
    '''
    def _ler_arquivo(self, path):

        arquivo = open(path, 'r')
        arquivo = arquivo.readlines()
        arquivo = [arquivo.replace("\n", "") for arquivo in arquivo]

        return arquivo

    '''
    Verifica a existencia do arquivo a partir de seu nome na pasta 'instances'
    '''
    def _get_arquivo_path (self):

        path = None
        nome_arquivo = 'InstanciaTeste.txt'

        # Navega pela pasta a procura do arquivo
        for root, dirs, files in os.walk("assets/"):
            if path is None: # Evita encontrar dois arquivos com o mesmo nome
                for file in files:
                    if nome_arquivo in file:
                        print("\nArquivo encontrado!")
                        path = os.path.join(root, file)
                        print("Caminho: " + path +"\n")
                        loop = False
                        break # Evita encontrar dois arquivos com o mesmo nome
        
        if path is None:
            sys.exit("\nArquivo nao encontrado! Certifique-se de estar rodando o sistema a partir da pasta raiz 'source'!\n")
        
        return path

    '''
    Retorna o arquivo
    '''
    def get_arquivo_em_lista(self):
        return self.__arquivo

    '''
    Retorna o numero de clientes
    '''
    def get_qtd_clientes(self):
        return int(self.__arquivo[0])-int(self.__arquivo[1])

    '''
    Retorna o numero de sub-regioes
    '''
    def get_qtd_sub_regioes(self):
        return int(self.__arquivo[1])

    '''
    Retorna a quantidade de tipos diferentes de veiculos
    '''
    def get_qtd_tipos_veiculos(self):
        return int(self.__arquivo[2])

    '''
    Retorna o numero de horas da jornada diaria
    '''
    def get_horas_jornada_diaria(self):
        return int(self.__arquivo[3])

    '''
    Retorna a posicao (coordenadas) das sub-regioes
    '''
    def get_coordenadas_sub_regioes(self):

        qtd_sub_regioes = self.get_qtd_sub_regioes()

         # Calcula a linha do arquivo que corresponde a ultima sub regiao       
        ultima_linha_regiao = 4 + qtd_sub_regioes

        coordenadas = self.__arquivo[4:ultima_linha_regiao]

        # Quebra cada linha transformando cada um de seus únicos elementos em uma lista de elementos 
        coordenadas = [list(coordenadas.split()) for coordenadas in coordenadas] 
        
        # Remove os elementos com valor '0'
        coordenadas = [[i for i in nested if i != '0'] for nested in coordenadas]

        # Transforma as coordenadas em tipo numerico (float)
        coordenadas = [[float(y) for y in x] for x in coordenadas]

        return coordenadas

    def get_clientes(self):
        qtd_clientes = self.get_qtd_clientes()
        ultima_linha_clientes = 9 + qtd_clientes

        clientes = self.__arquivo[9:ultima_linha_clientes]

        # Quebra cada linha transformando cada um de seus únicos elementos em uma lista de elementos 
        clientes = [list(clientes.split()) for clientes in clientes] 

        return clientes