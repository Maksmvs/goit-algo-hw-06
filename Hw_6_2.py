import networkx as nx
import matplotlib.pyplot as plt

def dfs_paths(graph, start, goal, path=None):
    if path is None:
        path = [start]
    if start == goal:
        yield path
    for next_node in set(graph.neighbors(start)) - set(path):
        yield from dfs_paths(graph, next_node, goal, path + [next_node])

def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next_node in set(graph.neighbors(vertex)) - set(path):
            if next_node == goal:
                yield path + [next_node]
            else:
                queue.append((next_node, path + [next_node]))

def plot_graph(G, paths=None):
    pos = nx.spring_layout(G)
    
    edge_kwds = {'arrowsize': 20}

    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='lightcoral', edge_color='gray')
    
    if paths:
        for i, (path_edges, color, distances) in enumerate(paths):
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color=color, width=2, arrows=True, **edge_kwds)
            nx.draw_networkx_edge_labels(G, pos, edge_labels={(edge[0], edge[1]): f"{edge[2]['distance']} м" for edge in G.edges(data=True)}, font_size=8, font_color=color)
            nx.draw_networkx_labels(G, pos, {node: node for node in G.nodes}, font_color='black', font_size=8, font_weight='bold')
            plt.text(0.5, -0.1 - i * 0.1, f'(Відстань: {distances} м)', color=color, fontsize=10, transform=plt.gca().transAxes)

    plt.title("Мапа відпочинку та розваг")
    plt.show()

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

start_node = "Магазин"
end_node = "Бібліотека"

dfs_result = list(dfs_paths(G, start_node, end_node))
bfs_result = list(bfs_paths(G, start_node, end_node))

edge_distances = {(edge[0], edge[1]): edge[2]['distance'] for edge in G.edges(data=True)}

paths_to_visualize = []

if dfs_result:
    dfs_path_edges = [(dfs_result[0][i], dfs_result[0][i+1]) for i in range(len(dfs_result[0])-1)]
    dfs_distances = sum(edge_distances.get(edge, edge_distances.get((edge[1], edge[0]))) for edge in dfs_path_edges)
    paths_to_visualize.append((dfs_path_edges, 'red', dfs_distances))

if bfs_result:
    bfs_path_edges = [(bfs_result[0][i], bfs_result[0][i+1]) for i in range(len(bfs_result[0])-1)]
    bfs_distances = sum(edge_distances.get(edge, edge_distances.get((edge[1], edge[0]))) for edge in bfs_path_edges)
    paths_to_visualize.append((bfs_path_edges, 'green', bfs_distances))

plot_graph(G, paths=paths_to_visualize)

