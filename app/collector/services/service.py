import yaml
import requests
from pprint import pprint
from lxml import html
from lxml import etree
from dataclasses import  dataclass
from dataclasses import   asdict


from schema import Anuncio 
from schema import Utilizador
from schema import Avaliacao

class Collect:
    def __init__(self):
        self.tree_html_anuncio = ''
        self.tree_html_morada = ''
        self.fuul_tree_html_location = []
        self.fuul_tree_html_annoumcement = []

    def _request_http(self, site ):       
        response_http_url = requests.get(site)

        tree_html =  html.fromstring(response_http_url.text)

        return tree_html          
    def extraction_content_user(self, tree_html_location, user):

        telefone = self._get_xpath_value(tree_html_location, user['utilizador']['telefone'])
        morada = self._get_xpath_value(tree_html_location, user['utilizador']['endereco'])
        horario = self._get_xpath_value(tree_html_location, user['utilizador']['hora_funcionamento'])
        nome_empresa =  user['utilizador']['nome_empresa']   
        utilizador = Utilizador (
            telefone = telefone,
            endereco = morada,
            hora_funcionamento = horario,
            nome_empresa = nome_empresa
        )    
        return asdict(utilizador)
    
    def extraction_content_annouct(self, tree_html_announcement, announcement, indice):
        
        marca = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['marca'])
        numero_passageiro = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['numero_passageiro'])
        combustivel = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['combustivel'])
        ano = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['ano'])
        preco = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['preco'])
        taxa_extra = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['caucao'])
        transmissao = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['transmissao'])
        nome_empresa =  announcement['anuncio']['nome_empresa']   

        anuncio = Anuncio (
            marca = self.error_tratament_index_error(marca,indice),
            numero_passageiro = self.error_tratament_index_error(numero_passageiro,indice),
            combustivel = self.error_tratament_index_error(combustivel,indice),
            ano = self.error_tratament_index_error(ano,indice),
            preco =  self.error_tratament_index_error(preco,indice),
            caucao = self.error_tratament_index_error(taxa_extra,indice),
            transmissao = self.error_tratament_index_error(transmissao,indice),  
            nome_empresa = nome_empresa
        )
        
        return asdict(anuncio)
    
    def error_tratament_index_error (self,campo,indice):
        try:
            return campo[indice]
        except IndexError:
            campo = None
            return campo
                
    def extraction_number_annouct(self,tree_html_announcement, announcement):
        """
            Extrair o numero de anuncios registados no html.
            Sabendo o xpaht completo da informação especifica relativa as marca de viaturas no tree_html. 
            saberemos quantos anuncios tem o html .  

            Parametros:
                Tree_html_announcement: árvore completa do html de anuncios de viaturas 
                announcement: Xpaht permite localizar a informação especifica relativa a marcas de viaturas 
                          na pagina html em analise

            Retorna:
                numero_anuncios: retorna o numero de anuncios.    
        """
        marca = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['marca'])
        numero_anuncios = len(marca)
        print ("OLIME PORRA ", numero_anuncios ,type(numero_anuncios)) 
        return numero_anuncios

    def _get_xpath_value(self,tree_html,xpath):
        value = tree_html.xpath(xpath)
        return value 
     
    def _request_http_offline(self, content_link):             
        with open(content_link, 'r', encoding='utf-8') as f:
            content_html = f.read()
        
        full_tree_html =  html.fromstring(content_html)
          
        return full_tree_html
    
    def config_file (self):
        try:
            with open('/mnt/c/Users/HP/datacolletor/app/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
    
        return config_link