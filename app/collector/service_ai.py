import os
from dotenv import load_dotenv
import requests
from datetime import datetime, timezone
import json

from langchain.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_openai import ChatOpenAI
import openai

openai.api_key = "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"
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
    ResponseSchema(name="disponibilidade", description="Disponibilidade atual do carro"),
]

output_parser = StructuredOutputParser.from_response_schemas(schemas)
format_instructions = output_parser.get_format_instructions()

prompt = PromptTemplate(
    template="""
Você é um extrator de dados inteligente. Receberá um conteúdo HTML de uma página de rent-a-car e deve extrair apenas os dados relevantes do anúncio do carro com os seguintes campos:

{format_instructions}

HTML:
{html}
""",
    input_variables=["html"],
    partial_variables={"format_instructions": format_instructions},
)

url = "https://caetano-cpv.caetano.africa/campanhas/rent-a-car/"
html = requests.get(url).text

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0, openai_api_key = openai.api_key)

final_prompt = prompt.format(html=html)

output = llm.predict(final_prompt)
try:
    anuncio = output_parser.parse(output)
    anuncio["data"] = str(datetime.now())
    anuncio["audit_user"] = "langchain"
    anuncio["audit_timestamp"] = str(datetime.now(timezone.utc))

    print(json.dumps(anuncio, indent=4, ensure_ascii=False))
except Exception as e:
    print("Erro ao interpretar:", e)
    print("Resposta bruta:", output)
