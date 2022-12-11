#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os
import pandas as pd


# In[6]:


print('Diretório inicial: {}'.format(os.getcwd()))
os.chdir('C:/Users/ppomp/Documents/Python')


# In[7]:


print('novo diretório: {}'.format(os.getcwd()))


# In[8]:


tabela_bruta_comercio_internacional = pd.read_csv('WTD_trabalho.py.csv', sep = ',',  encoding = 'ISO-8859-1')


# In[60]:


#aumentar número de linhas e colunas visualizáveis para ter um entendimento melhor da base d 
pd.options.display.max_rows = 30
pd.options.display.max_columns = 24
pd.options.display.max_colwidth = 100

tabela_bruta_comercio_internacional


# In[39]:


##### criar uma lista com os nomes do todas as colunas para ter um acesso rápido a tais informações
cabeçalho = list(tabela_bruta_comercio_internacional.columns.values)
print(cabeçalho)

#analisando a tabela, ficoou claro que ela mistura diferentes tipos de informações, para lidar com isso,
#criar lista de categorias, com o intuito de dividir o data frame em vários outros para cada categoria,
#obtendo, assim, informações mais úteis

#para tanto, transformar a primeira coluna em uma lista
lista_categorias_repetidos = tabela_bruta_comercio_internacional['Indicator Category'].tolist()

#os dados repetidos e o excesso de linhas torna difícil se aproveitar da lista
#eliminar elementos repetidos com list comp.
lista_categorias = []
[lista_categorias.append(categoria) for categoria in lista_categorias_repetidos if categoria not in lista_categorias]
print(lista_categorias)


# In[57]:


#tendo as categorias, usar df.loc para construir tabelas separadas de cada categoria

index_df_ic = tabela_bruta_comercio_internacional.loc[tabela_bruta_comercio_internacional['Indicator Category'] == str(lista_categorias[0])]
index_df_ic


# In[58]:


values_df_ic = tabela_bruta_comercio_internacional.loc[tabela_bruta_comercio_internacional['Indicator Category'] == str(lista_categorias[1])]
values_df_ic


# In[61]:


serv_comerc_df_ic = tabela_bruta_comercio_internacional.loc[tabela_bruta_comercio_internacional['Indicator Category'] == str(lista_categorias[2])]
serv_comerc_df_ic


# In[64]:


lista_tipos_indices_repet = index_df_ic['Indicator'].tolist()
lista_tipos_indices = []
[lista_tipos_indices.append(indice) for indice in lista_tipos_indices_repet if indice not in lista_tipos_indices]
print(lista_tipos_indices)


# In[65]:


lista_ind_valores_comerc_repet = values_df_ic['Indicator'].tolist()
lista_ind_valores_comerc = []
[lista_ind_valores_comerc.append(critério) for critério in lista_ind_valores_comerc_repet if critério not in lista_ind_valores_comerc]
print(lista_ind_valores_comerc)


# In[66]:


lista_cs_ind_rep = serv_comerc_df_ic['Indicator'].tolist()
lista_cs_ind = []
[lista_cs_ind.append(critério) for critério in lista_cs_ind_rep if critério not in lista_cs_ind]
print(lista_cs_ind)


# In[70]:


print('indicadores de índice: ',len(lista_tipos_indices))
print('indicadores de valores comerciais: ',len(lista_ind_valores_comerc))
print('indicadores de serviços comerciais: ',len(lista_cs_ind))

