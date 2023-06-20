import streamlit as st
import os
import numpy as np  
import pandas as pd
import tabula as tb
import os
from pdfminer.high_level import extract_text


st.markdown('''
              <h4 style='text-align: center'> Gerador de tabela PSS </h4>
              <div style='background-color: lightgreen; font-weight: bold'>
              <p style='text-align: center; font-weight: bold'>Antes de Gerar a tabela com as informações do PSS são necessárias as seguintes ações: </p>
              <ol style='font-weight: bold'>
                <li>Vá até a unidade 'C:' do seu computador e crie uma pasta chamada 'pss' (tudo minúsculo)</li>
                <li>Para chegar até essa pasta, no Windows, abra o Explorador de Arquivos e digite na barra de endereços: c:\</li>
                <li>Salve o arquivo .pdf gerado no CACOCONPSS na pasta que foi criada anteriormente</li>
                <!--
                <li>O arquivo .html contendo a tabela será salvo nessa mesma pasta após você clicar no botão abaixo</li>
                -->
              </ol>
              </div>
              <br>
              ''', unsafe_allow_html=True)


def cabecalho_tabela(nome_pdf):
  with open(f"{nome_pdf}.html", "w", encoding="utf-8") as pss:
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
    

def corpo_tabela(dados_pss, ano, nome_pdf):
  with open(f"{nome_pdf}.html", "a") as pss:
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

def fechamento_tabela(nome_pdf):
  with open(f"{nome_pdf}.html", "a") as pss:
    pss.write(f'''</tbody>
              </table>''')

# Fazer download de arquvios
def baixar_arquivos(nome_do_arq):
  
      try:
          with open(str(nome_do_arq), "rb") as file:
              st.download_button(
                  label="CLIQUE AQUI PARA GERAR E BAIXAR A TABELA",
                  data=file,
                  file_name=nome_do_arq,
                  mime="text/html")
      except:
          st.error("ARQUIVO NÃO LOCALIZADO! REPITA O PROCESSO.")
 
      os.remove(nome_do_arq)

# limpar console
def limpa_tela():
  return os.system('Clear')

# capturar ano
def captura_ano(texto):
  inicio = texto.find("CONSULTA  :  ")
  termino = texto.find("                                                                    CONTINUA... ") - 3
  ano = texto[(inicio + 13):(inicio + 17)]
  return ano


def gerar_tabela_pss(nome_arq):
  # carregar o arquivo
  
  nome_do_arquivo = nome_arq
  os.chdir('/pss') 
  caminho = os.getcwd()
  arquivo = f'{caminho}/{nome_do_arquivo}'
  #print(caminho)

  
  # capturando caminho do arquivo
  path = arquivo
  tabela = tb.read_pdf(path, pages="all") # gerando uma lista com as tabelas
  # capturando ano do arquivo
  texto_arquivo = extract_text(path)
  ano_arquivo = captura_ano(texto_arquivo)
  ano = ano_arquivo
  
  # Gerando cabeçalho do arquivo
  cabecalho_tabela(nome_arq[:-4])
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
    corpo_tabela(dados_pss, ano, nome_arq[:-4])

    # incrementando o ano
    ano = int(ano) + 1



  # verificando se todos os arquivos já foram processados, caso sim encerra o programa.
  fechamento_tabela(nome_arq[:-4])
  baixar_arquivos(f'{nome_arq[:-4]}.html')
  # with open("tabela_pss.html", "r") as tbl:
  #   tbl_pss = tbl.read().strip()
  # st.markdown(tbl_pss, unsafe_allow_html=True)
  

uploaded_file = st.file_uploader("Selecione o arquivo na pasta 'c:\pss': ")
if uploaded_file is not None:
  # col_1, col_2, col_3 = st.columns([1,2,1])
  # with col_1:
  #   pass
  # with col_2:
  #   gerar_tab = st.button("CLIQUE AQUI PARA GERAR A TABELA")
  # with col_3:
  #   pass
  # if gerar_tab:
  gerar_tabela_pss(uploaded_file.name)
      





    