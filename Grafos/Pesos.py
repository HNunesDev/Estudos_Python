from PIL import Image
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt



grafo = Graph(directed = False)
grafo.add_vertices(4)
grafo.add_edges([(0,1), (2,3), (0,2), (0,3)])
grafo.vs['label'] = ['Abel','Bernardo','Carol','Dionisio']

#Definindo peso nas arestas, tornando o grafo ponderado
grafo.es['TipoAmizade'] = ['Amigo','Inimigo', 'Inimigo', 'Amigo']
grafo.es['weight'] = [1,2,1,3]
grafo.vs['type'] = ['Humanos']
grafo.vs['name'] = ['Amizade']

#Grafo com todas as caracteristas preenchidas
print(grafo)

plot(grafo, target='grafo.png', bbox=(300,300))
imagem = Image.open("grafo.png")
plt.imshow(imagem)
plt.axis('off')
plt.show()


