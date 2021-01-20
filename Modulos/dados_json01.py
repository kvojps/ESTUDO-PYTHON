
from dados import clientes_dicionario
import json

with open('clientes.json','w') as arquivo:
     json.dump(clientes_dicionario, arquivo, indent=4)

with open('clientes.json','r') as arquivo:
    dados = json.load(arquivo)

for chave, valor in dados.items():
    print(chave)
    print(valor)