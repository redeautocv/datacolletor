from datetime import datetime

import yaml
import requests
from pprint import pprint
from lxml import html
from lxml import etree
from dataclasses import  dataclass
from dataclasses import   asdict

from app.collector.models.anunciante import Anunciante
from app.collector.models.anuncio import Anuncio
from app.collector.models.autenticacao import Autenticacao

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

        nome = user['anunciante']['nome']
        sexo = self._get_xpath_value_user(tree_html_location, user['anunciante']['sexo'] )
        telefone = self._get_xpath_value_user(tree_html_location, user['anunciante']['telefone'])
        link =  user['anunciante']['link']
        email = self._get_xpath_value_user(tree_html_location, user['anunciante']['email'])
        foto = self._get_xpath_value_user(tree_html_location, user['anunciante']['foto'], )
        ilha = self._get_xpath_value_user(tree_html_location, user['anunciante']['ilha'])
        descricao = self._get_xpath_value_user(tree_html_location, user['anunciante']['descricao'])
        concelho = self._get_xpath_value_user(tree_html_location, user['anunciante']['concelho'])
        horario_funcionamento = self._get_xpath_value_user(tree_html_location, user['anunciante']['horario_funcionamento'])
        tipo = self._get_xpath_value_user(tree_html_location, user['anunciante']['tipo'])
        endereco = self._get_xpath_value_user(tree_html_location, user['anunciante']['endereco'])
        audit_user = "datacollector"

        audit_timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        anunciante = Anunciante(
            nome = nome,  
            sexo = sexo,
            telefone = telefone,
            link = link,
            email = email,
            foto = foto,
            ilha = ilha,
            descricao = descricao,
            concelho = concelho,
            horario_funcionamento = horario_funcionamento,
            tipo = tipo,
            endereco = endereco,
            audit_user = audit_user,
            audit_timestamp =  audit_timestamp

        )         
        return anunciante
    
    def extraction_content_annouct(self, tree_html_announcement, announcement, indice):
        
        marca = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['marca'], indice)
        numero_passageiro = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['numero_passageiro'], indice)
        combustivel = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['combustivel'], indice)
        ano = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['ano'], indice)
        preco = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['preco'], indice)
        caucao = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['caucao'], indice)
        fotografia = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['fotografia'], indice)
        gps = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['gps'], indice)
        ar_condicionado = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['ar_condicionado'], indice)
        transmissao = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['transmissao'], indice)
        disponibilidade = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['disponibilidade'], indice)
        modelo = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['modelo'], indice)
        data = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['data'], indice)
        audit_timestamp =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")   
        audit_user = "datacolletor" 

        
        anuncio = Anuncio (
            marca = marca, 
            modelo = modelo, 
            numero_passageiro = numero_passageiro, 
            combustivel= combustivel, 
            ano = ano, 
            preco = preco, 
            caucao = caucao, 
            fotografia = fotografia, 
            ar_condicionado = ar_condicionado,  
            gps = gps, 
            disponibilidade = disponibilidade, 
            transmissao = transmissao, 
            audit_user = audit_user,
            data = data, 
            audit_timestamp = audit_timestamp 
        )
        
        return anuncio
    
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
        #marca = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['marca'], indice=None)
        marca = tree_html_announcement.xpath(announcement['anuncio']['marca'])
        numero_anuncios = len(marca)
        return numero_anuncios

    def   _get_xpath_value(self,tree_html,xpath,indice):
        value = tree_html.xpath(xpath)
        try:
            if len(value) < 2:
                return value
            else:
                return value[indice] 
        except IndexError:
            return value
     
    def   _get_xpath_value_user(self,tree_html,xpath):
        value = tree_html.xpath(xpath)
        return value
    
    def _request_http_offline(self, content_link):             
        with open(content_link, 'r', encoding='utf-8') as f:
            content_html = f.read()
        
        full_tree_html =  html.fromstring(content_html)
          
        return full_tree_html
    
    def config_file (self):
        try:
            with open('/home/ruifortes/datacolletor/app/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
    
        return config_link
