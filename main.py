import statistics
import igraph as ig
import numpy as np
from functions import readGraph1, readGraph2, plotGraph, createGraph, getDegreeStatistics, getDistancesStatistics, getCCSizesStatistics, getClusterizationStatistics

# Rede 1: "network_db/download.tsv.chess/chess/out.chess"
# Rede 2: "network_db/download.tsv.radoslaw_email/radoslaw_email/out.radoslaw_email_email"
# Rede 3:

num_vertices, edges, weights = readGraph2()
g = createGraph(num_vertices, edges, weights)
# plotGraph(g, "email")
# getDegreeStatistics(g, "emails")
# getDistancesStatistics(g, "emails")
# getCCSizesStatistics(g, "emails")
# getClusterizationStatistics(g)

