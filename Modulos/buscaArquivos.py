import os

caminho_procura = input('Digite um caminho: ')
termo_procura = input('Digite o arquivo que deseja procurar: ')
contador = 0

def formata_tamanho(tamanho):
    kilo = 1024
    mega = 1024 ** 2
    giga = 1024 ** 3
    tera = 1024 ** 4

    if tamanho <= kilo:
        texto = 'bytes'
    elif tamanho < mega:
        tamanho /= kilo
        texto = 'KB'
    elif tamanho < giga:
        tamanho /= mega
        texto = 'MB'
    elif tamanho < tera:
        tamanho /= giga
        texto = 'GB'
    else:
        tamanho /= tera
        texto = 'TB'
    
    tamanho = round(tamanho, 2)
    return f'{tamanho} {texto}'

for raiz, pastas, arquivos in os.walk(caminho_procura):
    for arquivo in arquivos:
        if termo_procura in arquivo:
            try:
                contador += 1
                caminho_completo = os.path.join(raiz,arquivo)
                nome_arquivo, extensao_arquivo = os.path.splitext(arquivo)
                tamanho_arquivo = os.path.getsize(caminho_completo)
                
                print(' ')
                print('Arquivo encontrado:', arquivo)
                print('Caminho:', caminho_completo)
                print('Nome:', nome_arquivo)
                print('Extensão do arquivo:', extensao_arquivo)
                print('Tamanho:', formata_tamanho(tamanho_arquivo))
                print('-'*30)
            
            except PermissionError as e:
                print('Você não tem permissão para utilizar este arquivo.')
            except FileNotFoundError as e:
                print('Arquivo não encontrado')
            except Exception as e:
                print('Erro desconhecido', e)

print(f'{contador} arquivo(s) encontrado(s).')




        