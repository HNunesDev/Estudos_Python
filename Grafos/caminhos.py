from PIL import Image
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt

grafo = Graph(edges = [(0,2),(0,1),(1,4),(1,5),(2,3),(6,7),(3,7),(4,7),(5,6)], directed = True)
grafo.vs['label'] = ['A','B','C','D','E','F','G','H']
grafo.es['weight'] = [2,1,2,1,2,1,3,1]
grafo.es['label'] = [2,1,2,1,2,1,3,1]

caminho_vertice = grafo.get_shortest_path(0,7, output = 'vpath')
print(caminho_vertice)

#Caminho
caminho_arestaID = []
for n in caminho_arestaID[0]:
    caminho_arestaID.append(n)
print(f'O caminho é: {caminho_arestaID}')

distancia = 0
for e in grafo.es:
    if e.index in caminho_arestaID:
        distancia += grafo.es['weight']
print(f'A distancia é: {distancia}')

plot(grafo, target='grafo.png', bbox=(300,300))
grafoimg = Image.open('grafo.png')
plt.imshow(grafoimg)
plt.axis('off')
plt.show()
