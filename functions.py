import igraph as ig
import statistics
import matplotlib.pyplot as plt
import numpy as np

def findMax(arr):
    max_value = 0
    for tuple in arr:
        if tuple[0] > max_value:
            max_value = tuple[0]
        if tuple[1] > max_value:
            max_value = tuple[1]
    return max_value

def readGraph1():
    f = open("network_db/download.tsv.chess/chess/out.chess", "r")
    f.readline() # cabeçalho
    edges = []
    weights = []
    # aux = 1
    for line in f:
        # aux += 1
        # if aux < 1000:
        line = line.split('\t')[0].split(" ")
        edges.append((int(line[0]), int(line[1])))
        weights.append(int(line[2]))
    num_vertices = findMax(edges)
    return num_vertices, edges, weights

def readGraph2():
    f = open("network_db/download.tsv.radoslaw_email/radoslaw_email/out.radoslaw_email_email", "r")
    f.readline() # cabeçalho
    f.readline() # cabeçalho
    edges = []
    weights = []
    # aux = 1
    for line in f:
        # aux += 1
        # if aux < 1000:
        line = line.split(" ")
        edges.append((int(line[0]), int(line[1])))
        weights.append(1)
    num_vertices = findMax(edges)
    return num_vertices, edges, weights

def readGraph3():
    f = open("network_db/usairports", "r")
    f.readline() # cabeçalho
    f.readline() # cabeçalho
    edges = []
    weights = []
    for line in f:
        line = line.split(" ")
        edges.append((int(line[0]), int(line[1])))
        weights.append(int(line[2]))
    num_vertices = findMax(edges)
    print(num_vertices, len(edges))
    return num_vertices, edges, weights

def createGraph(n_vertices, edges, weights):
    g = ig.Graph(n_vertices, edges)
    g["title"] = "Chess Games"
    g.es["weights"] = weights
    return g

def plotGraph(g, name):
    # Note that attributes can be set globally (e.g. vertex_size), or set individually using arrays (e.g. vertex_color)
    fig, ax = plt.subplots(figsize=(5,5))
    ig.plot(
        g,
        target=ax,
        vertex_size=0.1,
        vertex_color=["steelblue"],
        vertex_frame_width=4.0,
        vertex_frame_color="white",
        vertex_label=g.vs.indices,
        vertex_label_size=7.0,
        edge_color=["#7142cf" if win == "1" else "salmon" for win in g.es["weights"]]
    )
    plt.show()
    fig.savefig(name + '.png')
    fig.savefig(name + '.jpg')
    fig.savefig(name + '.pdf')
    g.save(name + ".gml")
    g = ig.load(name + ".gml")
    
def plotCCDF(array, name):
    values, counts = np.unique(array, return_counts=True)
    ccdf = 1 - np.cumsum(counts) / len(array)
    fig, ax = plt.subplots(figsize=(5,5))
    plt.loglog(values, ccdf, marker='o', linestyle='-', color='b')
    plt.title("Complementary Cumulative Degree Distribution (CCDF)")
    plt.xlabel(name + " (log scale)")
    plt.ylabel("CCDF (log scale)")
    plt.grid(True)
    plt.show()
    fig.savefig(name + '_ccdf.png')

def getDegreeStatistics(g, name):
    degrees = g.degree()
    min_degree, max_degree = min(degrees), max(degrees)
    mean_distance, median_degree = (sum(degrees) / len(degrees)), sorted(degrees)[len(degrees) // 2]
    std_dev_degree = statistics.stdev(degrees)
    print(f"Graus (min/max/média/mediana/desvio_padrão): {min_degree, max_degree, mean_distance, median_degree, std_dev_degree}")
    plotCCDF(degrees, "Graus_" + name)

def getDistancesStatistics(g, name):
    distances = np.array(g.vs().distances())
    distances = distances.flatten()
    # Removemos distâncias infinitas
    distances = np.delete(distances, np.where(distances == float('inf')))
    min_distance, max_distance = min(distances), max(distances)
    mean_ccsize, median_distance = (sum(distances) / len(distances)), sorted(distances)[len(distances) // 2]
    std_dev_distance = statistics.stdev(distances) # Bug
    print(f"Distâncias (min/max/média/mediana/desvio_padrão): {min_distance, max_distance, mean_ccsize, median_distance, std_dev_distance}")
    plotCCDF(distances, "Distâncias_" + name)

def getCCSizes(g):
    CCsizes = []
    for cluster in g.clusters():
        CCsizes.append(len(cluster))
    return CCsizes

def getCCSizesStatistics(g, name):
    ccsizes = getCCSizes(g)
    min_ccsize, max_ccsize = min(ccsizes), max(ccsizes)
    mean_ccsize, median_ccsize = (sum(ccsizes) / len(ccsizes)), sorted(ccsizes)[len(ccsizes) // 2]
    std_dev_ccsize = statistics.stdev(ccsizes) # Bug
    print(f"Tamanho Componentes Conexas (min/max/média/mediana/desvio_padrão): {min_ccsize, max_ccsize, mean_ccsize, median_ccsize, std_dev_ccsize}")
    plotCCDF(ccsizes, "Tamanho_Componentes_Conexas_" + name)

def getBetwennessStatistics(g, name):
    betwenness = g.vs().betweenness()
    min_betwenness, maxn_betwenness = min(betwenness), max(betwenness)
    meann_betwenness, mediann_betwenness = (sum(betwenness) / len(betwenness)), sorted(betwenness)[len(betwenness) // 2]
    std_devn_betwenness = statistics.stdev(betwenness) # Bug
    print(f"Betwenness (min/max/média/mediana/desvio_padrão): {min_betwenness, maxn_betwenness, meann_betwenness, mediann_betwenness, std_devn_betwenness}")
    plotCCDF(betwenness, "Betwenness_" + name)

def getClusterizationStatistics(g):
    print(g.clusters())
    print("haf")