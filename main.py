import statistics
import igraph as ig
import numpy as np
from functions import readGraph1, readGraph2, readGraph3, createGraph, getBetwennessStatistics, getDegreeStatistics, getDistancesStatistics, getCCSizesStatistics, getClusterizationStatistics

# Rede 1: "network_db/download.tsv.chess/chess/out.chess"
# Rede 2: "network_db/download.tsv.radoslaw_email/radoslaw_email/out.radoslaw_email_email"
# Rede 3: "network_db/usairports"

num_vertices, edges, weights = readGraph3()
g = createGraph(num_vertices, edges, weights)
# plotGraph(g, "email")
# getDegreeStatistics(g, "flights")
# getDistancesStatistics(g, "flights")
# getCCSizesStatistics(g, "flights")
getBetwennessStatistics(g, "flights")
# getClusterizationStatistics(g)

