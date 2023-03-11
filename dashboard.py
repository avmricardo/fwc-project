from dash import Dash, html, dcc, Input, Output
import plotly.express as px
import pandas as pd
import datas as dt
import goals_functions as func

app = Dash(__name__)

fig = px.funnel()

app.layout = html.Div(children=[
    html.H1(children='Dataset da Copa do Mundo'),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Dropdown(dt.parametros, value=[
                 "Fase de grupos"], id='dropdown', multi=True),
    html.Div(id='dd-output-container'),

    dcc.Graph(
        id='graph',
        figure=fig
    ),

])


@app.callback(
    Output('graph', 'figure'),
    Input('dropdown', 'value')
)
def update_output(value):
    if value == []:
        return px.funnel()

    indices = []
    for i in value:
        indice = dt.parametros.index(i)
        indices.append(indice)

    fase = []
    for i in indices:
        fase += dt.fases_copa[i]

    times = func.selecoes(fase)
    razoes_times = func.razoes_gols_selecoes(fase, times)
    lista1 = zip(times, razoes_times)
    total = list(lista1)
    total = func.ordenar_lista(total)

    paises = []
    razoes = []
    for i in total:
        paises.append(i[0])
        razoes.append(i[1])

    fig = px.funnel(labels={"x": "Razões", "y": "Países"}, x=razoes, y=paises, width=1400,
                    height=900, title="Razões entre gols feitos e gols tomados por seleções")

    return fig


if __name__ == '__main__':
    app.run_server(debug=True)
