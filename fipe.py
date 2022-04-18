#lib para pegar dados da internet
from wsgiref import headers
import requests
import json
#biblioteca excel 
import xlsxwriter







headers_info = {'User-Agent': 'Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36'}
dados = requests.get(url='https://parallelum.com.br/fipe/api/v2/motorcycles/brands', headers=headers_info )

lista_dados = json.loads(dados.content)

documento_excel = xlsxwriter.Workbook('fipe001.xlsx')
planilha_excel = documento_excel.add_worksheet('MARCAS')

tamanho_lista = 1
planilha_excel.write(0, 0, "MODELO")
planilha_excel.write(0, 1, "CODIGO")
for modelo in lista_dados:
    #print(f"{marca.get('name')}   : {marca.get('code')}")
    planilha_excel.write(tamanho_lista, 0, modelo.get('name'))
    planilha_excel.write(tamanho_lista, 1, modelo.get('code'))
    tamanho_lista += 1
    
planilha_excel_motos = documento_excel.add_worksheet('MOTOS')

dados_modelo = requests.get(url="https://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models", headers=headers_info)

lista_modelo = json.loads(dados_modelo.content)
linha = 1


for modelo in lista_modelo:
    planilha_excel_motos.write(linha , 0, modelo.get('model'))
    planilha_excel_motos.write(linha , 1, modelo.get('code'))
    linha += 1

planilha_excel_fipe_yamaha = documento_excel.add_worksheet('FIPE - YAMAHA')
linha = 0
for modelo in lista_modelo:
    for ano in range(2007, 2009, 1):
        api = f"https://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models/{modelo.get('code')}/years/{ano}-1"
        #api = f"http://parallelum.com.br/fipe/api/v2/motorcycles/brands/74/models/{modelo.get('code')}/years/{ano}-1"
        # api = "http://parallelum.com.br/fipe/api/v2/motorcycles/brands/101/models/4571/years/2009-1"
        print(api)

        dados = requests.get(url=api, headers=headers_info)
        print(dados)

        if dados.status_code == 200:
            moto = json.loads(dados.content)
            planilha_excel_fipe_yamaha.write(linha, 0, moto.get('model'))
            planilha_excel_fipe_yamaha.write(linha, 1, moto.get('price') )  
            planilha_excel_fipe_yamaha.write(linha, 2, moto.get('fuel') )  
            planilha_excel_fipe_yamaha.write(linha, 3, moto.get('modelYear') )  
            linha += 1
        

documento_excel.close()  


