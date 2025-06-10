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

        telefone = self._get_xpath_value(tree_html_location, location['localizacao']['telefone'])
        morada = self._get_xpath_value(tree_html_location, location['localizacao']['morada'])
        horario = self._get_xpath_value(tree_html_location, location['localizacao']['horario'])
            
        data_content = DataContentLocation(telefone, morada, horario)
            
        return asdict(data_content)
    
    def extraction_content_annouct(self, tree_html_announcement, announcement):
        
        marca = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['marca'])
        numero_lugares = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['numero_lugares'])
        combustivel = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['combustivel'])
        ano = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['ano'])
        preco = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['preco'])
        taxa_extra = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['taxa_extra'])
        transmissao = self._get_xpath_value(tree_html_announcement, announcement['anuncio']['transmissao'])
        
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