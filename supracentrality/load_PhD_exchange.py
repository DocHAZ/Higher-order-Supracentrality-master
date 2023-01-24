

import networkx as nx
import numpy as np
from scipy import sparse


################################################
## Load temporal network 
################################################


def load_temporal_PhD_flow_graph(foldername):
    # load school names from file
#     file1 = open(foldername+'/EUAirTransportation_nodes(name)_ext.txt','r') 
    file1 = open(foldername+'/school_names.txt','r')
    graph = {}
    graph['nodenames'] = [x.strip() for x in file1]
    graph['N'] = len(graph['nodenames'])
    
    # load graph  from file
#     file2 = open(foldername+'/EUAirTransportation_multiplex_0.1_Adjust.txt','r')
#     file2 = open(foldername+'/PhD_exchange.txt','r')
    file2 = open(foldername+'/PhD_exchange_jq_m1_0.1.txt','r')
    edges = np.array(np.loadtxt(file2))
#     edges = np.array(np.loadtxt(file2),'int')
    graph['layer_names'] = [str(j) for j in np.unique(edges[:,3])]
#     print(graph['layer_names'],'layer_names')
    graph['T'] = len(graph['layer_names'])

    # a tensor in containing network adjacency matrix at each time
    graph['A_tensor'] = []
    for t in range(graph['T']):
        graph['A_tensor'].append(sparse.csr_matrix((graph['N'],graph['N'])))
    
    for edge in edges:
        node_A = int(edge[0])-1     
        node_B = int(edge[1])-1
        weight = edge[2]
#         print(edge[3],'3333333333')
#         edge[3]= int(edge[3])
#         print(int(edge[3]),'33333333331111111111111')
#         print(node_A,'node_A')
#         print(node_B,'node_B')
#         print(weight,'weight')
#         year_id   = np.where([s == str(edge[3]) for s in graph['layer_names']])[0][0]
        year_id   = np.where([s==str((edge[3])) for s in graph['layer_names']])[0][0]
#         print(int(edge[3]),'00000000')
#         print(year_id,'year_id')
#         year_id = int(year_id)
#         year_id = list(map(lambda x: int(x), year_id))      # year_id为x迭代的list,lambda输入x,输出int(x)

        graph['A_tensor'][year_id][node_A,node_B] += weight
        
    # Uncomment the following if you want to add self-edges of some small weight

    #for t,year in enumerate(graph['layer_names']):
    #    graph['A_tensor'][year_id] =  graph['A_tensor'][year_id] + sparse.eye(graph['N'])*10**-14
    
    return graph




################################################
## Load time-aggregated network 
################################################

def load_PhD_flow_graph(data_folder):

    # load school names from file
#     file1 = open(data_folder+'/EUAirTransportation_nodes(name)_ext.txt','r')
    file1 = open(data_folder+'/school_names.txt','r')

    graph = {}
    graph['nodenames'] = [x.strip() for x in file1] 
    graph['N'] = len(graph['nodenames'])
    
    # load graph  from file
#     file2 = open(data_folder+'/EUAirTransportation_multiplex_0.1_Adjust.txt','r') 
#     file2 = open(data_folder+'/PhD_exchange.txt','r')
    file2 = open(data_folder+'/PhD_exchange_jq_m1_0.1.txt','r')
#     edges = np.array(np.loadtxt(file2),'int')
    edges = np.array(np.loadtxt(file2))
#     print(edges,'edges_all')
    #graph['A'] = zeros((graph['N'],graph['N']))
    graph['A'] = sparse.csr_matrix((graph['N'],graph['N']))
#     print(graph['A'],'before_graphA')
    for edge in edges:
#         print(int(edge[0])-1)
        graph['A'][int(edge[0])-1,int(edge[1])-1] += edge[2]
#     print(graph['A'].shape[1],'after_graphA')
    # compute number of edges
    graph['M'] = np.sum(graph['A'])
#     print(graph['M'],'graphM')
    print('Loaded network with:') 
    print(str(graph['N']) + ' nodes') 
    print(str(int(graph['M'])) + ' edges') 

    return graph





# import networkx as nx
# import numpy as np
# from scipy import sparse


# ################################################
# ## Load temporal network 
# ################################################


# def load_temporal_PhD_flow_graph(foldername):
#     # load school names from file
#     file1 = open(foldername+'/school_names.txt','r') 
#     graph = {}
#     graph['nodenames'] = [x.strip() for x in file1]
#     graph['N'] = len(graph['nodenames'])
    
#     # load graph  from file
#     file2 = open(foldername+'/PhD_exchange.txt','r') 
#     edges = np.array(np.loadtxt(file2),'int')
#     graph['layer_names'] = [str(j) for j in np.unique(edges[:,3])]
#     graph['T'] = len(graph['layer_names'])

#     # a tensor in containing network adjacency matrix at each time
#     graph['A_tensor'] = []
#     for t in range(graph['T']):
#         graph['A_tensor'].append(sparse.csr_matrix((graph['N'],graph['N'])))
    
#     for edge in edges:
#         node_A = edge[0]-1     
#         node_B = edge[1]-1
#         weight = edge[2]
#         year_id   = np.where([s == str(edge[3]) for s in graph['layer_names'] ])[0][0]
#         graph['A_tensor'][year_id][node_A,node_B] += weight
    
#     # Uncomment the following if you want to add self-edges of some small weight

#     #for t,year in enumerate(graph['layer_names']):
#     #    graph['A_tensor'][year_id] =  graph['A_tensor'][year_id] + sparse.eye(graph['N'])*10**-14
    
#     return graph




# ################################################
# ## Load time-aggregated network 
# ################################################

# def load_PhD_flow_graph(data_folder):

#     # load school names from file
#     file1 = open(data_folder+'/school_names.txt','r') 

#     graph = {}
#     graph['nodenames'] = [x.strip() for x in file1]
#     graph['N'] = len(graph['nodenames'])
    
#     # load graph  from file
#     file2 = open(data_folder+'/PhD_exchange.txt','r') 
#     edges = np.array(np.loadtxt(file2),'int')
#     #graph['A'] = zeros((graph['N'],graph['N']))
#     graph['A'] = sparse.csr_matrix((graph['N'],graph['N']))
#     for edge in edges:
#         graph['A'][edge[0]-1,edge[1]-1] += edge[2]
        
#     # compute number of edges
#     graph['M'] = np.sum(graph['A'])
    
#     print('Loaded network with:') 
#     print(str(graph['N']) + ' nodes') 
#     print(str(int(graph['M'])) + ' edges') 

#     return graph




