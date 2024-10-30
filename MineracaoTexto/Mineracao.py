import matplotlib.pyplot as plt
import nltk
nltk.download('stopwords')
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import stopwords
from matplotlib.colors import ListedColormap
from wordcloud import WordCloud


corpus = PlaintextCorpusReader('C:\\Users\\henri\\Vscode\\Estudos_Python\\MineracaoTexto\\Arquivos', '.*', encoding='ISO-8859-1')

arquivo = corpus.fileids()
print(arquivo[0])

texto1 = corpus.raw('1.txt')
print(texto1)

#todo texto
todo_texto = corpus.raw()

palavras = corpus.words()
print(palavras[170])

print(len(palavras))

#Stopwords = palavras sem valor semantico
stops = stopwords.words('english')

mapa_cores = ListedColormap(['orange', 'green', 'red', 'blue'])

#Nuvem de palavras com até 100 com as stopwords
nuvem = WordCloud(background_color='white', colormap=mapa_cores, stopwords= stops, max_words=100)
nuvem_img = nuvem.generate(todo_texto)

# Representação em imagem
plt.imshow(nuvem_img, interpolation='bilinear')
plt.axis('off')
plt.show()


#mostrando as palavras mais frequentes
frequencia = nltk.FreqDist(palavras)
comum = frequencia.most_common(100)
print(comum)