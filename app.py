import streamlit as st
import os
import numpy as np  
import pandas as pd
import tabula as tb
import os
from pdfminer.high_level import extract_text

st.subheader("Gerador de tabela para PSS")

def cabecalho_tabela():
  with open("tabela_pss.html", "w", encoding="utf-8") as pss:
    pss.write(f'''
          <table border="1" cellpadding="0" cellspacing="0">
            <thead>
              <tr>
                  <td style="text-align: center; padding: 5px;">&nbsp;&nbsp;Ano&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Janeiro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Fevereiro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Março&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Abril&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Maio&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Junho&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Julho&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Agosto&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Setembro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Outubro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Novembro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Dezembro&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Grat.Natalina &nbsp;</td>
              </tr>
              <tr>
                  <td style="text-align: center; padding: 5px;">&nbsp;&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
                  <td style="text-align: center; padding: 5px;">&nbsp;Valor&nbsp;</td>
              </tr>
            </thead>
            <tbody border="1" cellpadding="0" cellspacing="0">''')
    

def corpo_tabela(dados_pss, ano):
  with open("tabela_pss.html", "a") as pss:
    pss.write(f'''
                  <tr>
                    <td style="text-align: center; padding: 5px;">&nbsp;{ano}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[0][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[1][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[2][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[3][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[4][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[5][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[6][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[7][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[8][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[9][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[10][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[11][2]}&nbsp;</td>
                    <td style="text-align: center; padding: 5px;">&nbsp;{dados_pss[12][2]}&nbsp;</td>
                  </tr>''')

def fechamento_tabela():
  with open("tabela_pss.html", "a") as pss:
    pss.write(f'''</tbody>
              </table>''')

# Fazer download de arquvios
def baixar_arquivos(nome_arq):
  pass

# limpar console
def limpa_tela():
  return os.system('Clear')

# capturar ano
def captura_ano(texto):
  inicio = texto.find("CONSULTA  :  ")
  termino = texto.find("                                                                    CONTINUA... ") - 3
  ano = texto[(inicio + 13):(inicio + 17)]
  return ano


def gerar_tabela_pss():
  # carregar o arquivo
  
  os.chdir('/pss') 
  caminho = os.getcwd()
  arquivo = f'{caminho}/pss.pdf'

  
  # capturando caminho do arquivo
  path = arquivo
  tabela = tb.read_pdf(path, pages="all") # gerando uma lista com as tabelas
  # capturando ano do arquivo
  texto_arquivo = extract_text(path)
  ano_arquivo = captura_ano(texto_arquivo)
  ano = ano_arquivo
  
  # Gerando cabeçalho do arquivo
  cabecalho_tabela()
  # percorrendo tabelas
  for ind, tab in enumerate(tabela):
    # retirando coluna desnecessária
    tabela[ind] = tabela[ind].drop(columns=["Unnamed: 0"])

    # aqui seria bom colocar o procedimento de tirar a linha que está como cabeçalho e colocar dentro da tabela
    tabela[ind].loc[len(tabela[ind])] = [list(tabela[ind])[0], list(tabela[ind])[1], list(tabela[ind])[2], list(tabela[ind])[3]]# transformando cabeçalho em uma linha da tabela

    # Mudando nome das colunas (CABEÇALHO DA TABELA)
    tabela[ind].columns = ['MES', 'PSS APURADO', 'REMU', 'REMUNERACAO PSS']

    # retirando coluna desnecessária
    tabela[ind] = tabela[ind].drop(columns=["REMU"])

    # dicionário para guardar os dados
    dados_pss = []

    # colocando o mes de janeiro na primeira linha
    dados_pss.append([tabela[ind]['MES'][12].replace("_ ","").replace(" :","").replace(":",""), tabela[ind]["PSS APURADO"][12], tabela[ind]["REMUNERACAO PSS"][12]])
    
    # colocando as demais linhas dentro do dicionário
    for row in range(12):
        dados_pss.append([tabela[ind]['MES'][row].replace("_ ","").replace(" :","").replace(":",""), tabela[ind]["PSS APURADO"][row], tabela[ind]["REMUNERACAO PSS"][row]])

    # inserindo informações na tabela
    corpo_tabela(dados_pss, ano)

    # incrementando o ano
    ano = int(ano) + 1



  # verificando se todos os arquivos já foram processados, caso sim encerra o programa.
  fechamento_tabela()
  with open("tabela_pss.html", "r") as tbl:
    tbl_pss = tbl.read().strip()
  st.markdown(tbl_pss, unsafe_allow_html=True)
  # print("Arquivo gerado com sucesso! \n")
  # baixar_arquivos("tabela_pss.html")
      

gerar_tab = st.button("GERAR TABELA")
if gerar_tab:
    gerar_tabela_pss()
    