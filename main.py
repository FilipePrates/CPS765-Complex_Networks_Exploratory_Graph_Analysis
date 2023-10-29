import statistics
import igraph as ig
from functions import readGraph, createGraph, plotGraph, plotCCDF

num_vertices, edges, weights = readGraph()
g = createGraph(num_vertices, edges, weights)

# Get (Grau/Degree) statistics
degrees = g.degree()
min_degree, max_degree = min(degrees), max(degrees)
mean_degree, median_degree = (sum(degrees) / len(degrees)), sorted(degrees)[len(degrees) // 2]
std_dev = statistics.stdev(degrees)
print(f"Graus (min/max/média/mediana/desvio_padrão): {min_degree, max_degree, mean_degree, median_degree, std_dev}")
plotCCDF(degrees, "Graus_Xadrez")
# plotGraph(g)

# # Get (Distância/Distance) statistics
# degrees = g.degree()
# min_degree, max_degree = min(degrees), max(degrees)
# mean_degree, median_degree = (sum(degrees) / len(degrees)), sorted(degrees)[len(degrees) // 2]
# std_dev = statistics.stdev(degrees)
# print(f"Graus (min/max/média/mediana/desvio_padrão): {min_degree, max_degree, mean_degree, median_degree, std_dev}")
# plotCCDF(degrees, "Graus_Xadrez")
# # plotGraph(g)
