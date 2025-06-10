import yaml
import requests
from lxml import html,etree
from dataclasses import  dataclass, asdict
from pprint import pprint


from ..collector.models.models import Listing, Advertiser, Location 
from  ..collector.model_data.data_json import  DataGross
from  ..collector.model_data.data_annouct import  DataXpathAnnouncement
from  ..collector.model_data.data_location import  DataXpathLocation
from  .model_data.data_content_annouct import  DataContentAnnouncement
from  .model_data.data_content_location import  DataContentLocation

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

    def extraction_content_location(self, tree_html_location, location):
            
            data_xpath = DataXpathLocation( 
                location['localizacao']['telefone'],
                location['localizacao']['morada'],
                location['localizacao']['horario'],
            ) 
            
            telefone = self._get_xpath_value(tree_html_location, data_xpath.xpath_telefone)
            morada = self._get_xpath_value(tree_html_location, data_xpath.xpath_morada)
            horario = self._get_xpath_value(tree_html_location, data_xpath.xpath_telefone)
            
            data_content = DataContentLocation(telefone, morada, horario)
            
            return asdict(data_content)
    
    def extraction_content_annouct(self, tree_html_announcement, announcement):
        
        data_xpath = DataXpathAnnouncement( 
            announcement['anuncio']['marca'],
            announcement['anuncio']['numero_lugares'],
            announcement['anuncio']['combustivel'],
            announcement['anuncio']['ano'],
            announcement['anuncio']['preco'],
            announcement['anuncio']['taxa_extra'],
            announcement['anuncio']['transmissao'],
        ) 
        
        marca = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_marca)
        numero_lugares = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_numero_lugares)
        combustivel = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_combustivel)
        ano = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_ano)
        preco = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_preco)
        taxa_extra = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_taxa_extra)
        transmissao = self._get_xpath_value(tree_html_announcement, data_xpath.xpath_transmisão)
        
        data_content = DataContentAnnouncement(
            marca, numero_lugares, combustivel, ano, preco, taxa_extra, transmissao
        )
        
        return asdict(data_content)
            
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