import xmltodict
import os 
import pandas as pd

# função ler o xml
def pegar_infos(nome_arquivo, valores):
   # print(f"Informações Adquiridas de: {nome_arquivo}" )
    with open(f'nfs/{nome_arquivo}', "rb") as arquivo_xml:
        dic_arquivo = xmltodict.parse(arquivo_xml)
        infos_nf = dic_arquivo["retConsNFeLog"]["NFeLog"]["nfeProc"]["NFe"]["infNFe"]
        numero_nota = infos_nf ["@Id"]
        empresa_emissora = infos_nf ["emit"]['xNome']
        valor_total = infos_nf["total"]['ICMSTot']['vProd']
        valores.append([numero_nota, empresa_emissora, valor_total])



lista_arquivos = os.listdir("nfs")

#armazenando informações em uma tabela
colunas = ["numero_nota", "empresa_emissora", "valor_total"]
valores = []

for arquivo in lista_arquivos:
    pegar_infos(arquivo, valores)

#criando a tabela e exportando para o excel
tabela = pd.DataFrame(columns=colunas, data=valores)
tabela.to_excel("NotasFiscais.xlsx", index=False)