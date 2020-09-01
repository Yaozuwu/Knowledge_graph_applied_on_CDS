import pandas as pd
import numpy as np
import dgl
import sys

filename = '../Knowledge_graph_source_data/data_from_drkg.tsv'
kg = pd.read_csv(filename, sep ="\t", header=None)
triplets = kg.values.tolist()

entity_dictionary = {}
def insert_entry(entry, ent_type, dic):
    if ent_type not in dic:
        dic[ent_type] = {}
    ent_n_id = len(dic[ent_type])
    if entry not in dic[ent_type]:
         dic[ent_type][entry] = ent_n_id
    return dic

for triple in triplets:
    src = triple[0]
    split_src = src.split('::')
    src_type = split_src[0]
    dest = triple[2]
    split_dest = dest.split('::')
    dest_type = split_dest[0]
    insert_entry(src,src_type,entity_dictionary)
    insert_entry(dest,dest_type,entity_dictionary)

edge_dictionary = {}
for triple in triplets:
    src = triple[0]
    split_src = src.split('::')
    src_type = split_src[0]
    dest = triple[2]
    split_dest = dest.split('::')
    dest_type = split_dest[0]

    src_int_id = entity_dictionary[src_type][src]
    dest_int_id = entity_dictionary[dest_type][dest]

    pair = (src_int_id, dest_int_id)
    etype = (src_type, triple[1], dest_type)
    if etype in edge_dictionary:
        edge_dictionary[etype] += [pair]
    else:
        edge_dictionary[etype] = [pair]

graph = dgl.heterograph(edge_dictionary);


total_nodes = 0;
for ntype in graph.ntypes:
    print(ntype, '\t', graph.number_of_nodes(ntype));
    total_nodes += graph.number_of_nodes(ntype);
print("Graph contains {} nodes from {} node-types.".format(total_nodes, len(graph.ntypes)))



total_edges = 0;
for etype in graph.etypes:
    print(etype, '\t', graph.number_of_edges(etype))
    total_edges += graph.number_of_edges(etype);
print("Graph contains {} edges from {} edge-types.".format(total_edges, len(graph.etypes)))