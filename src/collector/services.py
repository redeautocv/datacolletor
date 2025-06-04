import yaml
import requests
from lxml import html,etree

from .models import Listing, Advertiser, Location 

class Collect:
    def __init__(self):
        self.tree_html_anuncio = ''
        self.tree_html_morada = ''
        self.foul_tree_html_location= []
        self.foul_tree_html_annoumcement = []


    def _request_http(self):
        foul_tree_html_location = []
        foul_tree_html_annoumcement = []
        headers = {
            'User-Agent': 'Mozilla/5.0'
        }
        try:
            with open('/mnt/c/Users/HP/datacolletor/src/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
        number_sites = len(config_link['sites']) 
        
        for contador in range (number_sites): 
            #print (config_link['sites'][0]['localizacao']['link'])
            try:
                link_announcements = config_link['sites'][contador]['localizacao']['link']
                link_location_companie = config_link['sites'][contador]['anuncio']['link']
           
            except requests.exceptions.HTTPError as errh:
                print("Erro HTTP:", errh)
            except requests.exceptions.ConnectionError as errc:
                print("Erro de conexão:", errc)
            except requests.exceptions.Timeout as errt:
                print("Timeout:", errt)
            except requests.exceptions.RequestException as err:
                print("Erro inesperado:", err)    
            
            response_http_url_location = requests.get(link_location_companie,headers=headers)
            response_http_url_annoucemnt = requests.get(link_announcements,headers=headers)

            foul_tree_html_location.append(  html.fromstring(response_http_url_location.text))
            foul_tree_html_annoumcement.append( html.fromstring(response_http_url_annoucemnt.text))
           
        #print("data",len(foul_tree_html_annoumcement))
    
              
        #xpath_expr = '/html/body/div[1]/div/main/div/section[2]/div/div[1]/div/div[1]/div/h2'
        #dados = foul_tree_html_annoumcement[0].xpath(xpath_expr)
        #print("UN", dados, len(dados))
        #print (config_link)
    
        return foul_tree_html_annoumcement, foul_tree_html_location

    def extraction_content(self,tree_html_anuncio,tree_html_morada):
        try:
            with open('/mnt/c/Users/HP/datacolletor/src/collector/etc/config.yaml') as file:
                config_link = yaml.safe_load(file)    
        except FileNotFoundError as e:
            print (f"Arquivo não encontrado :{e}")
        except  yaml.YAMLError as e:
            print (f"Arquivo não encontrado :{e}")
        
        number_sites = len(config_link['sites']) 
        
        #print ("Anuncio",len(tree_html_anuncio))
        #xpath_expr = '/html/body/div[1]/div/main/div/section[5]/div/div[1]/div/div[1]/div/h2/'
                     
        #dados = tree_html_anuncio[0].xpath(xpath_expr)
        #print("ddddois ", dados)
        
        listings_model = []
        location_model = []    
        for contable in range(number_sites): 
            #table localizacao
            xpath_telefone = config_link['sites'][contable ]['localizacao']['telefone']
            xpath_morada = config_link['sites'][contable ]['localizacao']['morada']
            xpath_horario = config_link['sites'][contable ]['localizacao']['horario']
            #table anuncio
            xpath_marca = config_link['sites'][contable ]['anuncio']['marca']
            print ( "teste",config_link['sites'][contable ]['anuncio']['marca'])    
            xpath_numero_lugares = config_link['sites'][contable ]['anuncio']['numero_lugares']
            
            xpath_combustivel = config_link['sites'][contable ]['anuncio']['combustivel']
            
            xpath_taxa_extra = config_link['sites'][contable ]['anuncio']['taxa_extra']
            
            xpath_preco = config_link['sites'][contable]['anuncio']['preco']
            
            xpath_ano = config_link['sites'][contable]['anuncio']['Ano']

            xpath_transmisão = config_link['sites'][contable]['anuncio']['transmissão']    

            try:
                content_telefone = tree_html_morada[contable].xpath(xpath_telefone) 
            except etree.XPathEvalError as e :
                content_telefone = ''
            
            try:
                content_morada = tree_html_morada[contable].xpath(xpath_morada) 
            except etree.XPathEvalError as e :
                content_horario = '' 
            
            try:
                content_marca = tree_html_anuncio[contable].xpath(xpath_marca) 
            except etree.XPathEvalError as e :
                content_marca = ''
            
            try:
                content_numero_lugares = tree_html_anuncio[contable].xpath(xpath_numero_lugares) 
            except etree.XPathEvalError as e :
                content_numero_lugares = '' 
            
            try:
                content_taxa_extra = tree_html_anuncio[contable].xpath(xpath_taxa_extra) 
            except etree.XPathEvalError as e :
                content_taxa_extra = ''
            try:
                content_preco = tree_html_anuncio[contable].xpath(xpath_preco) 
            except etree.XPathEvalError as e :
                content_preco = ''
            
            try:
                content_ano = tree_html_anuncio[contable].xpath(xpath_ano)
            except etree.XPathEvalError as e :
                content_ano = ''
            
            try:
                content_transmissão = tree_html_anuncio[contable].xpath(xpath_transmisão)
            except etree.XPathEvalError as e :
                content_transmissão = ''

            try:
                content_combustivel = tree_html_anuncio[contable].xpath(xpath_combustivel)
            except etree.XPathEvalError as e :
                content_combustivel = ''

            contador_anuncios_total = len(content_marca)
            print("Olime ei porra ", content_marca)
            print("Olime ei porra ", content_preco)
            print("Olime ei porra ", content_numero_lugares)
            print("fuel type", contador_anuncios_total )

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
        
            contador_localizacao_total = len(content_telefone)
            for contador in range(contador_localizacao_total):
                Location_model = {
                    "message" : content_morada[-1].text,
                    "contact" : content_telefone[-1].text,
                    "start_hour" : content_horario[-1].text,
                }
                location_model.append(Location_model)
        
        return listings_model, location_model   
   