import igraph as ig
import matplotlib.pyplot as plt

def readGraph():
    f = open("network_db/download.tsv.chess/chess/out.chess", "r")
    print(f.readline()) # cabeçalho
    edges = []
    weights = []
    aux = 1
    for line in f:
        line = line.split('\t')[0].split(" ")
        edges.append((int(line[0]), int(line[1])))
        weights.append(int(line[2]))
    num_vertices = findMax(edges)
    print("finished")
    return num_vertices, edges, weights

def createGraph(n_vertices, edges, weights):
    g = ig.Graph(n_vertices, edges)
    g["title"] = "Chess Games"
    g.es["weights"] = weights
    return g

def plotGraph(g):
    # Plot in matplotlib
    # Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
    fig, ax = plt.subplots(figsize=(5,5))
    ig.plot(
        g,
        target=ax,
        layout="circle", # print nodes in a circular layout
        vertex_size=0.1,
        vertex_color=["steelblue"],
        vertex_frame_width=4.0,
        vertex_frame_color="white",
        vertex_label=g.vs.indices,
        vertex_label_size=7.0,
        edge_color=["#7142cf" if win == "1" else "salmon" for win in g.es["weights"]]
    )

    plt.show()

    # Save the graph as an image file
    fig.savefig('chess_network.png')
    fig.savefig('chess_network.jpg')
    fig.savefig('chess_network.pdf')

    # Export and import a graph as a GML file.
    g.save("chess_network.gml")
    g = ig.load("chess_network.gml")

def findMax(arr):
    max_value = 0
    for tuple in arr:
        print(tuple)
        if tuple[0] > max_value:
            max_value = tuple[0]
        if tuple[1] > max_value:
            max_value = tuple[1]
    return max_value

num_vertices, edges, weights = readGraph()
g = createGraph(num_vertices, edges, weights)

# Get (Grau/Degree) statistics
degrees = g.degree()
min_degree, max_degree = min(degrees), max(degrees)
mean_degree, median_degree = (sum(degrees) / len(degrees)), sorted(degrees)[len(degrees) // 2]
print(f"Graus (min/max/média/mediana): {min_degree, max_degree, mean_degree, median_degree}")
# plotGraph(g)
