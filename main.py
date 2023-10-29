import statistics
import igraph as ig
import numpy as np
from functions import readGraph, createGraph, getDistancesStatistics, getCCs

num_vertices, edges, weights = readGraph()
g = createGraph(num_vertices, edges, weights)

# getDistancesStatistics(g)
getCCs(g)

