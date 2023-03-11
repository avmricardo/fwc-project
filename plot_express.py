import pandas as pd
import datas as dt
import goals_functions as func
import plotly.express as px

total = list(zip(dt.selecoes, func.razoes_gols_selecoes(dt.valores, dt.selecoes)))
total = func.ordenar_lista(total)

paises = []
razoes = []
for i in total:
    paises.append(i[0])
    razoes.append(i[1])

fig = px.funnel(labels={"x": "Razões", "y": "Países"}, x=razoes, y=paises,
                title="Razões entre gols feitos e gols tomados por seleções durante toda a copa do mundo")
fig.show()
