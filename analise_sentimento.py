import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from googletrans import Translator
translator = Translator()

#Text Analyzes

# Quando roda script a primeira vez:
nltk.download('vader_lexicon')
sia = SentimentIntensityAnalyzer()


def ntlk_analise(texto_full):
    # Tem textos que tem imagem e torna-se impossível a tradução, resultando em bug
    try:
    #Traduzindo para Ingles para fazer análise sentimento
        texto_traduzido = translator.translate(texto_full,dest='en').text    
        #Calculando Score 
        score = sia.polarity_scores(texto_traduzido)
        score_formatado = str(int(round(score['compound'],2) * 100)) + '%'
    except:
        score_formatado = 'Não Encontrado'

    return score_formatado