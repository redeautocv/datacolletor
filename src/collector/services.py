import yaml
import requests
from lxml import html

from .models import Listing, Advertiser, Location 

class Collect:
    def __init__(self):
        self.tree_html_anuncio = ''
        self.tree_html_morada = ''

    def _request_http(self):
        try:
            with open('/mnt/c/Users/HP/datacolletor/src/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
        
        url_localizacao_empresa = config_link['sites']['localizacao']['link']
        url_anuncio = config_link['sites']['anuncio']['link']
        response_http_url_localizacao = requests.get(url_localizacao_empresa)
        response_http_url_anuncio = requests.get(url_anuncio)
        foul_tree_html_localizacao = html.fromstring(response_http_url_localizacao.text)
        foul_tree_html_anuncio = html.fromstring(response_http_url_anuncio.text)

        return foul_tree_html_anuncio,foul_tree_html_localizacao

    def extraction_content(self,tree_html_anuncio,tree_html_morada):
        try:
            with open('/mnt/c/Users/HP/datacolletor/src/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
        
        #table localizacao
        xpath_telefone = config_link['sites']['localizacao']['telefone']
        xpath_morada = config_link['sites']['localizacao']['morada']
        xpath_horario = config_link['sites']['localizacao']['horario']
        #table anuncio
        xpath_marca = config_link['sites']['anuncio']['marca']
        xpath_numero_lugares = config_link['sites']['anuncio']['numero_lugares']
        xpath_combustivel = config_link['sites']['anuncio']['combustivel']
        xpath_taxa_extra = config_link['sites']['anuncio']['taxa_extra']
        xpath_preco = config_link['sites']['anuncio']['preco']

        content_telefone = tree_html_morada.xpath(xpath_telefone)
        content_morada = tree_html_morada.xpath(xpath_morada)
        content_horario = tree_html_morada.xpath(xpath_horario)
        content_marca = tree_html_anuncio.xpath(xpath_marca)
        content_numero_lugares = tree_html_anuncio.xpath(xpath_numero_lugares)
        content_combustivel = tree_html_anuncio.xpath(xpath_combustivel)
        content_taxa_extra = tree_html_anuncio.xpath(xpath_taxa_extra)
        content_preco = tree_html_anuncio.xpath(xpath_preco)
        
        contador_anuncios_total = len(content_marca)
        contador_localizacao_total = len(content_telefone)
        print(contador_localizacao_total)
        listings_model = []
        location_model = []    

        for contador in range(contador_anuncios_total):
            Listings_model = { 'listings':{
                "model" : content_marca[contador].text, 
                "price" : content_preco[contador].text,
                #extra_fees = content_taxa_extra[contador].text,
                "passenger_number" : content_numero_lugares[contador].text,
                "fuel_type" : content_combustivel[contador].text
                }
            }
            listings_model.append(Listings_model)
        
        for contador in range(contador_localizacao_total):
            Location_model = {
                "message" : content_morada[-1].text,
                "contact" : content_telefone[-1].text,
                "start_hour" : content_horario[-1].text,
            }
            location_model.append(Location_model)
        
        return listings_model, location_model   