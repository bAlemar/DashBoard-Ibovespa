#Bibliotecas
import dash
from dash import dcc
import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Output, Input, State
import plotly.express as px
import plotly.graph_objects as go
import yfinance
from scraping import scraping_titulo_noticia, scraping_texto_noticia
from analise_sentimento import ntlk_analise

app = dash.Dash(__name__,external_stylesheets=[dbc.themes.BOOTSTRAP],meta_tags=[{'content':'width-device,initial-scale=1.0'}])



# LISTAS

options_stock = ['WEGE3.SA','PETR4.SA','CEAB3.SA']
simbolo_pesquisa = ['WEG','petrobras','C%26A']

# GRIDS (linha,coluna)

grid12 = [
        html.P('Selecione o ativo',style={'color':'white','text-align': 'center','margin-top':'20px'}),
        dcc.Dropdown(id='stock',options = options_stock,value=options_stock[1]),
        html.Div(children=[html.Div(id='grafico_stock')])
        ]

grid13 = [
    html.H1('Notícias',style={'color':'white','text-align':'center','margin-top':'20px'}),
    html.Div(children=[html.Div(id='Noticias',style={'margin-top':'20px'})]),
]


# APP 
app.layout = html.Div([
    dbc.Row([
        dbc.Col([], width=1),
        dbc.Col(grid12, style={'background-color': '#303030'}), 
        dbc.Col(grid13, style={'background-color': '#303030','margin-left':'30px'}),  
        dbc.Col([], width=1)
    ], style={'background-color': '#303030',
              }),  
])

#Fazer parada para os 2 aparecerem no mesmo tempo
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
                    low=df['Low'], close=df['Close'])
                        ])

    fig.update_layout(xaxis_rangeslider_visible=False, plot_bgcolor='#303030', paper_bgcolor='#303030', font_color='white')

    grafico_stock = dcc.Graph(figure=fig)
    return [grafico_stock]

@app.callback(
[Output('Noticias','children')],
[Input('stock','value')]
)
def Noticias(stock):
    global dict_resultado
    pos = options_stock.index(stock)
    palavra_chave = simbolo_pesquisa[pos]
    dict_resultado = scraping_titulo_noticia(palavra_chave)
    layout_noticia = []
    for pos in range(len(dict_resultado)):
        #Calculando score análise sentimento
        texto = scraping_texto_noticia(dict_resultado['link'][pos])
        score = ntlk_analise(texto)
        
        elementos_noticia = html.Div([
            html.P(dict_resultado['categoria'][pos],style={'color':'white','font-size':'13px'}),
            html.A(dict_resultado['titulo'][pos], href=dict_resultado['link'][pos], target='_blank',style={'color':'white'}),
            html.H6(f'Score: {score}',style={'color':'white','margin-top':'10px'}),
            html.Hr()
        ])
        layout_noticia.append(elementos_noticia)


    return [layout_noticia]

if __name__ == '__main__':
    app.run_server(debug=True)
    