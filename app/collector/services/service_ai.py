import os
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from dataclasses import   asdict

from schema import Anuncio
from schema import Utilizador
load_dotenv()

class CollectIA: 
    def extraction_AI_content_annouct(self, url):
        os.api_key =  os.getenv('GOOGLE_API_KEY')
        schemas = [
            ResponseSchema(name="marca", description="Marca do carro"),
            ResponseSchema(name="modelo", description="Modelo do carro"),
            ResponseSchema(name="numero_passageiro", description="Número de passageiros em formato python integer"),
            ResponseSchema(name="combustivel", description="Tipo de combustívelSe null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="ano", description="Ano do carro,Tipo inteiro  "),
            ResponseSchema(name="preco", description="Preço do aluguel em formato python integer.Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="caucao", description="Valor da caução.Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="fotografia", description="URL da imagem do carro.Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="transmissao", description="Tipo de caixa de velocidade.Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="ar_condicionado", description="Tem ar condicionado? Se Sim ou Não?Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="gps", description="Tem GPS? Se Sim ou Não?Se null coloca no formato python 'None"),
            ResponseSchema(name="disponibilidade", description="Está Disponivel o carro para aluguer?Se Sim ou Não?"),
            ResponseSchema(name="audit_user", description="Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="nome_empresa", description="Se null coloca no formato python 'None' sem aspas  simples"),
            ResponseSchema(name="data", description="data de hoje extraido neste formato python time('%d/%m/%Y %H:%M')"),
            ResponseSchema(name="audit_timestamp", description="data de hoje foi extraido neste formato python time('%d/%m/%Y %H:%M')")
        ]

        output_parser = StructuredOutputParser.from_response_schemas(schemas)
        format_instructions = output_parser.get_format_instructions()

        prompt = PromptTemplate(
            template="""Você é um extrator de dados. Dado o HTML abaixo, extraia todas as informações uniformes dos anuncios de carros com os 
            seguintes campos no formato demostrado no JSON dicionaio para linguagem python :{format_instructions} HTML:{html} """, input_variables=["html"],
            partial_variables={"format_instructions": format_instructions},
        )

        url = url['anuncio']['link']
        html = requests.get(url).text

        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Ou "gemini-1.5-flash"
            temperature=0,
            convert_system_message_to_human=True,
        )

        final_prompt = prompt.format(html=html)
        output = llm.invoke(final_prompt)
        conteudo = output.content if hasattr(output, 'content') else str(output)
        conteudo_limpo = conteudo.strip().removeprefix("```json").removesuffix("```").strip()
        anuncios = json.loads(conteudo_limpo)
        print(anuncios) 
        return  anuncios
        
    def extraction_AI_content_user(self, url):    
        dados_user = []

        os.api_key =  os.getenv('GOOGLE_API_KEY')

        schemas = [
            ResponseSchema(name="telefone", description="Numero de telefones da empresa"),
            ResponseSchema(name="email", description="Email de contacto empresa"),
            ResponseSchema(name="endereco", description="endereços de funcionamento da empresa"),
            ResponseSchema(name="foto", description="fotografia da empresa"),
            ResponseSchema(name="hora_funcionamento", description="horario de funcionamenta da empresa"),
            ResponseSchema(name="concelho", description="concelhos de cabo verde que funciona a empresa"),
            ResponseSchema(name="ilha", description="ilhas de cabo verde que funciona a empresa"),
            ResponseSchema(name="nome", description="null"),
            ResponseSchema(name="sobrenome", description="null"),
            ResponseSchema(name="sexo", description="null"),
            ResponseSchema(name="tipo", description="null"),
            ResponseSchema(name="audit_user", description="null"),
            ResponseSchema(name="descricao", description="null"),
            ResponseSchema(name="nome_empresa", description="Nome da empresa "),
            ResponseSchema(name="audit_timestamp", description="Hora completa que foi extraido neste formato python agora.strftime('%d/%m/%Y %H:%M')")
        ]
        output_parser = StructuredOutputParser.from_response_schemas(schemas)
        format_instructions = output_parser.get_format_instructions()
    
        prompt = PromptTemplate(
            template="""
            Você é um extrator de dados. Dado o HTML abaixo, extraia todas as informações uniformes dos localização da empresa  com os seguintes campos no formato 
            demostrado no JSON  :{format_instructions} HTML:{html}""",
            input_variables=["html"],
            partial_variables={"format_instructions": format_instructions},
        )

        url = url['utilizador']['link']
        html = requests.get(url).text
    
        llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash",  # Ou "gemini-1.5-flash"
            temperature=0,
            convert_system_message_to_human=True,
        )

        final_prompt = prompt.format(html=html)
        output = llm.invoke(final_prompt)
        conteudo = output.content if hasattr(output, 'content') else str(output)
        conteudo_limpo = conteudo.strip().removeprefix("```json").removesuffix("```").strip()
        
        dados_user = json.loads(conteudo_limpo)
        
        return self.type_data(*dados_user)
         
    def type_data(self, data):
         
         if type(data ) == dict:
              return data
         if type(data ) == list:
              return data
         
    def format_data(self, data):
        
        anuncio = Anuncio(
            marca = data["marca"], 
            modelo = data["modelo"], 
            numero_passageiro = data["numero_passageiro"], 
            combustivel= data["combustivel"], 
            ano = data["ano"], 
            preco = data["preco"], 
            caucao = data["caucao"], 
            fotografia = data["fotografia"], 
            ar_condicionado = data["ar_condicionado"],  
            gps = data["gps"], 
            disponibilidade = data["disponibilidade"], 
            transmissao = data["transmissao"], 
            nome_empresa = data["nome_empresa"], 
            audit_user = data["audit_user"], 
            audit_timestamp = data["audit_timestamp"] 
        )

        return asdict(anuncio)
    
    def format_data_user(self, user):
            utilizador = Utilizador(
                nome = user["nome"],
                sobrenome = user["sobrenome"],
                sexo = user["sexo"],
                telefone = user["telefone"],
                email = user["email"],
                foto = user["foto"],
                nome_empresa = user["nome_empresa"],
                descricao = user["descricao"],
                hora_funcionamento = user["hora_funcionamento"],
                concelho = user["concelho"],
                ilha = user["ilha"],
                endereco = user["endereco"],
                tipo = user["tipo"]
            )   

            return asdict(utilizador)
         