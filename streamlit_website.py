import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.set_page_config(layout='wide') # torna página maior
@st.cache(allow_output_mutation=True) # o dataset vai ser salvo na memória, economizando processo

def get_data(path):
    df = pd.read_csv(path)
    return df

path = 'datasets/dados_tratados.csv'
df = get_data(path)


# vamos remover a coluna de urls, pois é irrelevante para a análise
df = df.drop(['url'], axis=1)
st.title('QuintoAndar: Análise de dados')
st.header('Dataset colhido em anúncios da cidade de São Paulo')
st.write(df)
st.header('Análise descritiva de cada feature')
st.write(df.describe())


# Filtrar análise por bairro
df_2 = df #salvando o original
df = df.loc[df['bairro'] == 'Higienópolis']

# O seguinte groupby agrupa as colunas 'bairro' e 'total', calculando a média e colocando em ordem ascendente através da coluna 'total'.
df_bairro = df_2[['bairro', 'total']].groupby(['bairro']).mean().sort_values('total').reset_index()

# Vamos plotar um gráfico de barras que relaciona os bairro e a média do valor total de cada um deles
st.header('Média do valor de aluguel do imóvel (R$) por bairro')
fig = px.histogram(df_bairro, x='bairro', y='total', nbins=19)
st.plotly_chart(fig, use_container_width=True)

# Vamos plotar gráficos que dizem a distribuição de algumas features importantes
df_quarto = df.groupby('quarto')['total'].agg(np.median).reset_index() # coluna quarto e seus preços totais correspondentes
df_banheiro = df.groupby('banheiro')['total'].agg(np.median).reset_index() # coluna banheiro e seus preços totais correspondentes
df_metragem = df.groupby('metragem')['total'].agg(np.median).reset_index() # coluna metragem e seus preços totais correspondentes

# Preço por metragem
st.header('Preço do aluguel por metragem')
fig = px.line(df_metragem, x='metragem', y='total')
st.plotly_chart(fig, use_container_width=True)

c1, c2 = st.columns(2) # criando duas colunas

# Imóveis por quartos
c1.header('Número de imóveis por quartos')
fig = px.histogram(df, x='quarto', nbins=19)
c1.plotly_chart(fig, use_container_width=True)

# Preços por quartos
c2.header('Média do aluguel por número de quartos')
fig = px.histogram(df_quarto, x='quarto', y='total', nbins=19)
c2.plotly_chart(fig, use_container_width=True)

c3, c4 = st.columns(2) # criando duas colunas

# Imóveis por banheiros
c3.header('Número de imóveis por banheiros')
fig = px.histogram(df, x='banheiro', nbins=19)
c3.plotly_chart(fig, use_container_width=True)

# Preços por banheiros
c4.header('Média do aluguel por número de banheiros')
fig = px.histogram(df_banheiro, x='banheiro', y='total', nbins=19)
c4.plotly_chart(fig, use_container_width=True)


# https://www.youtube.com/watch?v=4gWs26AfFhQ&list=PLZlkyCIi8bMprZgBsFopRQMG_Kj1IA1WG&index=7&ab_channel=SejaUmDataScientist
# 1:09:20