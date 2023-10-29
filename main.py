import statistics
import igraph as ig
import numpy as np
from functions import readGraph, createGraph, getDegreeStatistics, getDistancesStatistics, getCCSizesStatistics

num_vertices, edges, weights = readGraph()
g = createGraph(num_vertices, edges, weights)
# getDegreeStatistics(g)
# getDistancesStatistics(g)
# getCCSizesStatistics(g)

