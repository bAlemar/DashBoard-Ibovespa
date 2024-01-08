from bs4 import BeautifulSoup
import requests
import regex as re



def scraping_titulo_noticia(stock_name,qntd_noticias = 3):
    #Request
    url = f'https://braziljournal.com/?s={stock_name}'

    r = requests.get(url)

    #Scraping dos dados
    soup = BeautifulSoup(r.text,'html.parser')
    
    #Div do html que contém todas as noticias
    todas_noticias = soup.find_all(class_='wrap-bj')

    #Dicionário para armazenar as informações:
    dict_scraping = {
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
            dict_scraping['titulo'].append(elementos_titulo.a.text.strip())
            dict_scraping['link'].append(elementos_titulo.a['href'])
            dict_scraping['categoria'].append(elemento_categoria.a.text.strip())
    return dict_scraping

def scraping_texto_noticia(link):
    # Há notícias com link /play/ antes que possui class que contém texto diferente
    # Para isso foi criado condições caso contenha /play/ na url ou não.
    
    #Request
    r = requests.get(link)
    soup = BeautifulSoup(r.text,'html.parser')
    
    # Palavra chave 
    key_word = r'/play/'    
    resultado = re.search(key_word,link)
    
    #Variável que armazenará o texto
    texto_full = ''
    
    #Condição de link
    if resultado:
        noticia = soup.find_all(class_='boxarticle-infos-text')[0]
        paragrafos = noticia.find_all('p')

    else:
        noticia = soup.find_all(class_='post-content-text')[0]
        paragrafos = noticia.find_all('p')
    
    #Juntando todos os paragrafos da noticia
    for parag in paragrafos:
        texto_full += parag.text
    
    return texto_full
