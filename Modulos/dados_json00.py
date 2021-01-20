"""
Json é um formato de troca de dados entre sistemas e programas muito 
leve e de fácil utilização. Bastante utilizado por Apis.
"""

from dados import *
import json

# Transformando um dict em um objeto Json
dados_json = json.dumps(clientes_dicionario, indent=4)
# print(dados_json)

# Transformando um objeto Json em um dict
dicionario = json.loads(clientes_json)

for chave, valor in dicionario.items():
    print(chave)
    print(valor)