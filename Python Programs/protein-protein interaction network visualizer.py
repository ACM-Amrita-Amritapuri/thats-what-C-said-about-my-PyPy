import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm

def read(file):
    r=open(file)
    data = [l.split('\t') for l in r]
    df = pd.DataFrame(data[1:-1], columns = data[0]) 
    interactions = df[['preferredName_A', 'preferredName_B', 'score']]
    return interactions

def graph(interactions):
    G=nx.Graph()
    interactions = np.array(interactions)
    for i in range(len(interactions)):
        interaction = interactions[i]
        a = interaction[0]
        b = interaction[1]
        w = float(interaction[2]) 
        G.add_weighted_edges_from([(a,b,w)])
    return G

def viz(G):
    pos = nx.spring_layout(G)
    graph_colormap = cm.get_cmap('plasma')
    c = rescale([G.degree(v) for v in G],0.0,0.9) 
    c = [graph_colormap(i) for i in c]
    bc = nx.betweenness_centrality(G)
    s =  rescale([v for v in bc.values()],1500,7000)
    ew = rescale([float(G[u][v]['weight']) for u,v in G.edges],0.1,4)
    ec = rescale([float(G[u][v]['weight']) for u,v in G.edges],0.1,1)
    ec = [graph_colormap(i) for i in ec]
    plt.figure(figsize=(15,15),facecolor=[1,1,1,1])
    nx.draw_networkx(G, pos=pos, with_labels=True, node_color=c, node_size=s,edge_color= ec,width=ew,
                     font_color='white',font_weight='bold',font_size='9')
    plt.axis('off')
    plt.show()

# Protien Network Data can be downloaded from string-db.org
viz(graph(read('<replace the text with file name>')))
