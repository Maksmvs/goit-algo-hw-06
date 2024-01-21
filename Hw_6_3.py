import networkx as nx
import matplotlib.pyplot as plt
from prettytable import PrettyTable

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

for edge in G.edges(data=True):
    edge[2]['weight'] = edge[2]['distance']

all_shortest_paths = dict(nx.all_pairs_dijkstra_path(G))

table = PrettyTable()
table.field_names = ["Відправна вершина", "Кінцева вершина", "Найкоротший шлях", "Відстань (м)"]

for source_node, paths in all_shortest_paths.items():
    for target_node, path in paths.items():
        if source_node != target_node:
            distance = nx.shortest_path_length(G, source=source_node, target=target_node, weight='weight')
            table.add_row([source_node, target_node, path, distance])

print(table)
