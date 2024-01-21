import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

locations = ["Магазин", "Парк", "Ресторан", "Кінотеатр", "Бібліотека"]
connections = [("Магазин", "Парк", {"distance": 200}), 
               ("Магазин", "Ресторан", {"distance": 150}),
               ("Парк", "Ресторан", {"distance": 100}), 
               ("Ресторан", "Кінотеатр", {"distance": 120}),
               ("Кінотеатр", "Бібліотека", {"distance": 180}),
               ("Парк", "Бібліотека", {"distance": 250})]

G.add_nodes_from(locations)
G.add_edges_from(connections)

node_colors = ['skyblue' for _ in G.nodes]

pos = nx.spring_layout(G) 
edge_labels = {(i, j): f"{data['distance']} м" for i, j, data in G.edges(data=True)}

nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color=node_colors, arrowsize=20, edge_color='gray')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
plt.title("Мапа відпочинку та розваг")
plt.show()

print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступінь вершин:")
for node in G.nodes:
    print(f"{node}: {G.degree[node]}")
