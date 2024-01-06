from bs4 import BeautifulSoup
import requests

def scraping_noticia(stock_name,qntd_noticias = 3):
    #Request
    url = f'https://braziljournal.com/?s={stock_name}'

    r = requests.get(url)

    #Scraping dos dados
    soup = BeautifulSoup(r.text,'html.parser')
    
    #Div do html que contém todas as noticias
    todas_noticias = soup.find_all(class_='wrap-bj')

    #Dicionário para armazenar as informações:
    dict_url = {
        'titulo' : [],
        'link' : [],
        'categoria' : []
    }
    
    #Looping para interagir com cada notícia
    for i in todas_noticias:
        
        # Titulo e url    
        elementos_titulo = i.find_all('h2', class_='boxarticle-infos-title')[:qntd_noticias]
        
        # Tópico da noticia 
        elemento_categoria = i.find_all('p', class_='boxarticle-infos-tag')[:qntd_noticias]
    
        # Looping com os elementos para pegar informações de cada noticia
        for elementos_titulo, elemento_categoria in zip(elementos_titulo, elemento_categoria):
            dict_url['titulo'].append(elementos_titulo.a.text.strip())
            dict_url['link'].append(elementos_titulo.a['href'])
            dict_url['categoria'].append(elemento_categoria.a.text.strip())
    return dict_url