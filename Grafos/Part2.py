from PIL import Image
from igraph import Graph
from igraph import plot
import matplotlib.pyplot as plt

#Grafo nao direcionado
grafo1 = Graph(edges = [(0,1), (1,2), (2,3), (3,0)], directed = False)
grafo1.vs['label'] = range(grafo1.vcount())

plot(grafo1, target="grafo1.png", bbox=(300, 300))
print("Imagem do grafo criada")

print("======================")

print("Exibindo imgaem")
imagem1 = Image.open("grafo1.png")
plt.imshow(imagem1)
plt.axis('off')
plt.show()


#Criando um grafo e adicionando vertices e arestas através de funcoes
grafo2 = Graph(directed = False)
grafo2.add_vertices(10)
grafo2.add_edges([(0,1), (2,2), (2,3), (3,0)])
grafo2.vs['label'] = range(grafo2.vcount())

plot(grafo2, target="grafo2.png", bbox=(400,400))
imagem2 = Image.open("grafo2.png")
plt.imshow(imagem2)
plt.axis('off')
plt.show()



#Criando um grafo e dando nome aos vertices
grafo3 = Graph(directed = False)
grafo3.add_vertices(5)
grafo3.add_edges([(0,1), (1,2), (2,3), (3,4), (4,0), (0,2), (2,1)])
grafo3.add_vertex(5)
grafo3.add_vertex(6)
grafo3.vs['label'] = ['A','B','C','D','E','F','G']


plot(grafo3, target="grafo3.png", bbox=(300,300))
imagem3 = Image.open("grafo3.png")
plt.imshow(imagem3)
plt.axis('off')
plt.show()