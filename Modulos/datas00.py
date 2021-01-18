from datetime import datetime, timedelta

"""
strptime(str, fmt) -> Formatar uma string em data.
.strftime(fmt) -> Alterar o formato de uma data.
timestamp() -> Você pode transformar uma data em timestamp.
fromtimestamp() -> transformar um timestamp em data
timedelta() -> Trabalhar com intervalos de tempo

"""

# data = datetime(2021, 1, 18, 00, 19, 50 )
# print(data.strftime('%d/%m/%Y %H:%M:%S')) #DIRETIVAS

# data = datetime.strptime('18/01/2002','%d/%m/%Y')
# print(data)
# print(data.timestamp())
# data = datetime.fromtimestamp(1579316400.0)
# print(data)

data = datetime.strptime('20/04/2002 00:10:00', '%d/%m/%Y %H:%M:%S')
data = data + timedelta(days=5)
print(data.strftime('%d/%m/%Y %H:%M:%S'))
