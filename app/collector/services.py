import yaml
import requests
from lxml import html,etree
from dataclasses import  dataclass, asdict
from pprint import pprint


from ..collector.models.models import Listing, Advertiser, Location 
from  ..collector.model_data.data_json import  DataGross
from  ..collector.model_data.data_annouct import  DataXpathAnnouncement
from  ..collector.model_data.data_location import  DataXpathLocation
from  ..collector.model_data.data_content import  DataContent

class Collect:
    def __init__(self):
        self.tree_html_anuncio = ''
        self.tree_html_morada = ''
        self.foul_tree_html_location = []
        self.foul_tree_html_annoumcement = []

    def _request_http(self):       
        foul_tree_html_location = []
        foul_tree_html_annoumcement = []
        
        headers = {
             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        }
        
        config_link = self.config_file()
        number_sites = len(config_link['sites']) 
        
        for contador in range (number_sites): 
            try:
                link_announcements = config_link['sites'][contador]['localizacao']['link']
                link_location_companie = config_link['sites'][contador]['anuncio']['link']
      
                response_http_url_location = requests.get(link_location_companie, headers=headers)
                response_http_url_annoucemnt = requests.get(link_announcements, headers=headers)
  
                foul_tree_html_location.append(html.fromstring(response_http_url_location.text))
                foul_tree_html_annoumcement.append(html.fromstring(response_http_url_annoucemnt.text))
 
            except requests.exceptions.HTTPError as errh:
                print("Erro HTTP:", errh)
                return
            except requests.exceptions.ConnectionError as errc:
                print("Erro de conexão:", errc)
                return
            except requests.exceptions.Timeout as errt:
                print("Timeout:", errt)
                return
            except requests.exceptions.RequestException as err:
                print("Erro inesperado:", err)
                return    

        return foul_tree_html_annoumcement, foul_tree_html_location

    def extraction_content(self,tree_html_anuncio,tree_html_morada):
        config_link = self.config_file()
        number_sites = len(config_link['sites']) 
        
        for contable in range(number_sites): 
            locations_xpath = self._extract_content_confink_links_locations(config_link, contable)
            annouc_xpath = self._extract_content_confink_links_announcement(config_link, contable)
           
            data_contents = DataContent(
                self._exception_tratament_XPathEvalError_tree_html_locations(tree_html_morada,contable, locations_xpath.xpath_telefone),
                self._exception_tratament_XPathEvalError_tree_html_locations(tree_html_morada,contable, locations_xpath.xpath_morada),
                self._exception_tratament_XPathEvalError_tree_html_locations(tree_html_morada,contable, locations_xpath.xpath_horario),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_marca),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_numero_lugares),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_combustivel),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_ano),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_preco),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_taxa_extra),
                self._exception_tratament_XPathEvalError_tree_html_annoucement(tree_html_anuncio,contable, annouc_xpath.xpath_transmisão),
            
            )
            
            contador_anuncios_total = len(data_contents.content_marca) 
            json = []
            print("O numero de sites", contador_anuncios_total)
            try:
                for contador in range(contador_anuncios_total):           
                        datas = {  
                            "model" : self._exception_tratament_index(data_contents.content_marca, contador), 
                            "price" : self._exception_tratament_index(data_contents.content_preco, contador),
                            #extra_fees = content_taxa_extra[contador].text,
                            "passenger_number" : self._exception_tratament_index(data_contents.content_numero_lugares, contador),
                            "fuel_type"  : self._exception_tratament_index(data_contents.content_combustivel, contador),
                            "ano" : self._exception_tratament_index(data_contents.content_ano,contador),
                            "message" : data_contents.content_morada,
                            "tipo_negocio" : config_link['sites'][contable]['anunciante']['tipo_negocio'],
                            "nome_empresa" : config_link['sites'][contable]['anunciante']['nome_empresa'],
                            "contact" : data_contents.content_telefone,
                            "start_hour" : data_contents.content_horario,
                            "transmissao" : self._exception_tratament_index(data_contents.content_transmissão, contador),                   
                        }
                        print(datas)

                json.append(datas)          
 
            except Exception as e :
                print(e)
        return json
    
    def _exception_tratament_index(self, data, position):
        try:
            return data[position].text
        except  IndexError as e:
            return ''
        else:
            return data[position].text
 
    def _exception_tratament_XPathEvalError_tree_html_annoucement(self, tree_html, position, xpath):
        try:
            return tree_html[position].xpath(xpath)
        except etree.XPathEvalError as e :
            return ''
        else:
            return tree_html[position].xpath(xpath)
 
    def _exception_tratament_XPathEvalError_tree_html_locations(self, tree_html, position, xpath):
        try:
            return tree_html[position].xpath(xpath)
        except etree.XPathEvalError as e :
            return ''
        else:
            return tree_html[position].xpath(xpath)
         
    def _extract_content_confink_links_locations(self, config_link, position):
        locations_xpath = DataXpathLocation(
            config_link['sites'][position]['localizacao']['telefone'],
            config_link['sites'][position]['localizacao']['morada'],
            config_link['sites'][position]['localizacao']['horario'],
        )
        return locations_xpath 

    def _extract_content_confink_links_announcement(self, config_link, position):
        annouc_xpath = DataXpathAnnouncement(            
            config_link['sites'][position]['anuncio']['marca'],
            config_link['sites'][position ]['anuncio']['numero_lugares'],
            config_link['sites'][position ]['anuncio']['combustivel'],
            config_link['sites'][position ]['anuncio']['taxa_extra'],
            config_link['sites'][position]['anuncio']['preco'],
            config_link['sites'][position]['anuncio']['ano'],
            config_link['sites'][position]['anuncio']['transmissao']    
        )
        
        return annouc_xpath 

    def _tratament_index(self,data):
         return data   
     
    def _request_http_offline(self):
        foul_tree_html_location = []
        foul_tree_html_annoumcement = []
    
        try:
            with open('/mnt/c/Users/HP/datacolletor/app/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
        number_sites = len(config_link['sites']) 
        
        for contador in range (number_sites): 
            #print (config_link['sites'][0]['localizacao']['link'])
            try:
                file_announcements = config_link['sites'][contador]['localizacao']['link_offline']
                file_location_companie = config_link['sites'][contador]['anuncio']['link_offline']
           
            except requests.exceptions.HTTPError as errh:
                print("Erro HTTP:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Erro de conexão:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout:", errt)
            except requests.exceptions.RequestException as err:
                print("Erro inesperado:", err)    
            
            with open(file_announcements, 'r', encoding='utf-8') as f:
                    content_html_announcement = f.read()
                        
            with open(file_location_companie, 'r', encoding='utf-8') as f:
                    content_html_location = f.read()

        
            foul_tree_html_location.append(  html.fromstring(content_html_announcement))
            foul_tree_html_annoumcement.append( html.fromstring(content_html_location))
          
        return foul_tree_html_annoumcement, foul_tree_html_location
    
    def config_file (self):
        try:
            with open('/mnt/c/Users/HP/datacolletor/app/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
    
        return config_link