import time  
import json
from datetime import datetime
from  ..collector.models.collector import  DataCollector

def create(data_groos):
    agora = datetime.now()
    time_Now = agora.strftime("%d/%m/%Y %H:%M:%S")

    novo_registro = DataCollector (
        data_coleta = time_Now,
        nome_empresa = "",
        dados_anuncios = data_groos, 
        dados_localizacao = data_groos,
    )            
     
    dbt.session.add(novo_registro)
    dbt.session.commit()




