#Bibliotecas
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Output, Input, State
import plotly.express as px
import plotly.graph_objects as go
import yfinance
from scraping import scraping_noticia

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[{'content':'width-device,initial-scale=1.0'}])

# LISTAS

options_stock = ['WEGE3.SA','PETR4.SA','CEAB3.SA']
simbolo_pesquisa = ['WEG','petrobras%20ação','C%26A']

# GRIDS

grid12 = [
        html.P('Selecione o ativo'),
        dcc.Dropdown(id='stock',options = options_stock),
        html.Div(children=[html.Div(id='grafico_stock')])
        ]

grid13 = [
    html.H1('Notícias'),
    html.Div(children=[html.Div(id='Noticias')])
]

# APP 

app.layout = html.Div([
    dbc.Row([
        # dbc.Col([],width=1),
        dbc.Col(grid12),      
        dbc.Col(grid13),      
        dbc.Col([],width=1)
    ])

])

@app.callback(
 [Output('grafico_stock','children')],
 [Input('stock','value')]
)

def grafico(stock):
    # Carregando dados da yfinance
    df = yfinance.download(stock,
                        start='2023-01-01',
                        )

    fig = go.Figure(data=[go.Candlestick(x=df.index,
                    open=df['Open'], high=df['High'],
                    low=df['Low'], close=df['Adj Close'])
                        ])

    fig.update_layout(xaxis_rangeslider_visible=False)

    grafico_stock = dcc.Graph(figure=fig)
    return [grafico_stock]

@app.callback(
[Output('Noticias','children')],
[Input('stock','value')]
)
def Noticias(stock):
    pos = options_stock.index(f'{stock}')
    palavra_chave = simbolo_pesquisa[pos]
    dict_resultado = scraping_noticia(palavra_chave)

    layout_noticia = []
    for pos in range(len(dict_resultado)):
        elementos_noticia = html.Div([
            html.P(dict_resultado['categoria'][pos]),
            html.A(dict_resultado['titulo'][pos], href=dict_resultado['link'][pos], target='_blank'),
            html.Hr()
        ])
        layout_noticia.append(elementos_noticia)

    return [layout_noticia]





if __name__ == '__main__':
    app.run_server(debug=True)