import os
import sys

class Arquivo(object):

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
        nome_arquivo = 'instancia'

        # Navega pela pasta a procura do arquivo
        # for root, dirs, files in os.walk("../instances"):
        for root, dirs, files in os.walk("C:/Users/Breno/Desktop/graph-theory-practical-challenge/instances"):
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
        return int(self.__arquivo[0])

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