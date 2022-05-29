import networkx as nx
import matplotlib.pyplot as plt

def draw_graph(G):
  pos = nx.spring_layout(G)
  nx.draw_networkx(G, pos, with_labels=True, font_weight='bold')
  labels = nx.get_edge_attributes(G, 'weight')
  nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
  plt.show()

def getMinFlow(G, path):
    min_flow = 100
    for i in range(0, len(path)-1):
        temp = G[path[i]][path[i+1]]['weight']
        if (min_flow > temp): 
            min_flow = temp
    return min_flow


G = nx.DiGraph()
G.add_weighted_edges_from([('S', 'A', 4), ('A', 'B', 4), ('B', 'T', 2), ('S', 'C', 3), ('C', 'D', 6), ('D', 'T', 6), ('B', 'C', 3)])
draw_graph(G)

paths = nx.all_simple_paths(G, "S", "T")
max_flow = 0

for path in paths:
    temp = getMinFlow(G, path)
    print("For path ", path, " having min flow ", temp)
    for i in range (0, len(path) - 1):
        G[path[i]][path[i+1]]['weight'] -= temp
    draw_graph(G)
    max_flow += temp

print("Max Flow: ", max_flow)
