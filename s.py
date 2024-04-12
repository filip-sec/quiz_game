import networkx as nx
import matplotlib.pyplot as plt

# Create an empty graph
G = nx.Graph()

# Add nodes
nodes = ["Source Device (192.168.110.138)", "DNS Server (1.1.1.1)"]
G.add_nodes_from(nodes)

# Add edges
edges = [("Source Device (192.168.110.138)", "DNS Server (1.1.1.1)")]
G.add_edges_from(edges)

# Draw the network
pos = nx.spring_layout(G)  # positions for all nodes
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")
plt.title("Network Topology")
plt.show()
