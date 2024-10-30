from PIL import Image
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt


#Edges sao as arstas
grafo1 = Graph(edges = [(0,1), (1,2), (2,3), (3,0)], directed = True)
grafo1.vs['label'] = range(grafo1.vcount())
print(grafo1)


#Todos os vertices estao ligados
grafo2 = Graph(edges = [(0,1),(1,2),(2,3),(3,0),(3,2),(2,1),(1,0),(0,3)])
grafo2.vs['label'] = range(grafo2.vcount())
plot(grafo2, target="grafo2.png", bbox=(300, 300))
print("Salvo em imagem do grafo 2")

img = Image.open("grafo2.png")
plt.imshow(img)
plt.axis('off')  # Ocultar os eixos
plt.show()

#Grafo com laço
grafo3 = Graph(edges = [(0,1), (1,2), (2,3), (3,0), (1,1)], directed = True)
grafo3.vs['label'] = range(grafo3.vcount())
plot(grafo3, target="grafo3.png", bbox=(300, 300))
print("Salvo imagem 3")

img2 = Image.open("grafo3.png")
plt.imshow(img2)
plt.axis('off')
plt.show()