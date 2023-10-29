import statistics
import igraph as ig
import numpy as np
from functions import readGraph, createGraph, plotGraph, plotCCDF

num_vertices, edges, weights = readGraph()
g = createGraph(num_vertices, edges, weights)

# # # Get (Distância/Distance) statistics
# # Removemos distâncias infinitas
# distances = np.array(g.vs().distances())
# distances = distances.flatten()
# distances = np.delete(distances, np.where(distances == float('inf')))
# print(len(distances))
# min_distance, max_distance = min(distances), max(distances)
# mean_distance, median_distance = (sum(distances) / len(distances)), sorted(distances)[len(distances) // 2]
# # std_dev_distance = statistics.stdev(distances)
# print(f"Distâncias (min/max/média/mediana/desvio_padrão): {min_distance, max_distance, mean_distance, median_distance}")
# plotCCDF(distances, "Distâncias_Xadrez")
# plotGraph(g)
