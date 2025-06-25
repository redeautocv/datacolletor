import os
import json
from datetime import datetime, timezone
from dotenv import load_dotenv

import requests
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

def extraction_AI_content_annouct(url):
    os.api_key =  os.getenv('GOOGLE_API_KEY')

    schemas = [
        ResponseSchema(name="marca", description="Marca do carro"),
        ResponseSchema(name="modelo", description="Modelo do carro"),
        ResponseSchema(name="numero_passageiro", description="Número de passageiros"),
        ResponseSchema(name="combustivel", description="Tipo de combustível"),
        ResponseSchema(name="ano", description="Ano do carro"),
        ResponseSchema(name="preco", description="Preço do aluguel"),
        ResponseSchema(name="caucao", description="Valor da caução"),
        ResponseSchema(name="fotografia", description="URL da imagem do carro"),
        ResponseSchema(name="caixa_velocidade", description="Tipo de caixa de velocidade"),
        ResponseSchema(name="ar_condicionado", description="Tem ar condicionado?"),
        ResponseSchema(name="gps", description="Tem GPS?"),
        ResponseSchema(name="disponibilidade", description="Está Disponivel o carro para aluguer?"),
        ResponseSchema(name="transmissao", description="É Manual, automatico ou outra configuração? "),
        ResponseSchema(name="audit_user", description="null"),
        ResponseSchema(name="Nome_empresa", description="Nome da empresa "),
        ResponseSchema(name="data", description="data disponivel para aluguel do carro "),
        ResponseSchema(name="audit_timestamp", description="Hora completa que foi extraido neste formato python agora.strftime('%d/%m/%Y %H:%M')")
    ]

    output_parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = output_parser.get_format_instructions()

    prompt = PromptTemplate(
        template="""Você é um extrator de dados. Dado o HTML abaixo, extraia todas as informações uniformes dos anuncios de carros com os 
        seguintes campos no formato demostrado no JSON:{format_instructions} HTML:{html} """, input_variables=["html"],
        partial_variables={"format_instructions": format_instructions},
    )

    url = url['anuncio']['link']
    html = requests.get(url).text

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",  # Ou "gemini-2.5-flash"
        temperature=0,
        convert_system_message_to_human=True,
    )

    final_prompt = prompt.format(html=html)
    output = llm.invoke(final_prompt)
    conteudo = output.content if hasattr(output, 'content') else str(output)
    limpo = conteudo.strip().removeprefix("```json").removesuffix("```").strip()

    print (limpo)
    return limpo


def extraction_AI_content_user(url):    
    os.api_key =  os.getenv('GOOGLE_API_KEY')

    schemas = [
        ResponseSchema(name="telefone", description="Numero de telefones da empresa"),
        ResponseSchema(name="email", description="Email de contacto empresa"),
        ResponseSchema(name="endereco", description="endereços de funcionamento da empresa"),
        ResponseSchema(name="foto", description="fotografia da empresa"),
        ResponseSchema(name="Hora_funcionamento", description="horario de funcionamenta da empresa"),
        ResponseSchema(name="concelho", description="concelhos de cabo verde que funciona a empresa"),
        ResponseSchema(name="ilha", description="ilhas de cabo verde que funciona a empresa"),
        ResponseSchema(name="nome", description="null"),
        ResponseSchema(name="sobrenome", description="null"),
        ResponseSchema(name="tipo", description="null"),
        ResponseSchema(name="audit_user", description="null"),
        ResponseSchema(name="nome_empresa", description="Nome da empresa "),
        ResponseSchema(name="audit_timestamp", description="Hora completa que foi extraido neste formato python agora.strftime('%d/%m/%Y %H:%M')")
    ]
    output_parser = StructuredOutputParser.from_response_schemas(schemas)
    format_instructions = output_parser.get_format_instructions()
   
    prompt = PromptTemplate(
        template="""
        Você é um extrator de dados. Dado o HTML abaixo, extraia todas as informações uniformes dos localização da empresa  com os seguintes campos no formato 
        demostrado no JSON:{format_instructions} HTML:{html}""",
        input_variables=["html"],
        partial_variables={"format_instructions": format_instructions},
    )

    url = url['utilizador']['link']
    html = requests.get(url).text
  
    llm = ChatGoogleGenerativeAI(
        model="gemini-2.5-flash",  # Ou "gemini-1.5-flash"
        temperature=0,
        convert_system_message_to_human=True,
    )

    final_prompt = prompt.format(html=html)
    output = llm.invoke(final_prompt)
    conteudo = output.content if hasattr(output, 'content') else str(output)
    conteudo_limpo = conteudo.strip().removeprefix("```json").removesuffix("```").strip()

    print (conteudo_limpo)
    return conteudo_limpo 
        

