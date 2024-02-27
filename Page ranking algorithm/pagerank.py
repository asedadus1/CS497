import array


def main():
    # Add nodes
    nodes = ['A', 'B', 'C', 'D']
    # Add edges
    edges = [('B', 'A'), ('B', 'C'), ('C', 'A'), ('D', 'A')]
    
    #empty set to store node that have an outgoing edges
    nodes_with_outgoing_edges = set()
    #this will store the number of outbound edges each node it have
    outbound_edges_count = [0] * len(nodes)

    #this loop will count how many out going linkes are in the graph
    for edge in edges:
        nodes_with_outgoing_edges.add(edge[0])
        sorce_node = edge[0]
        sorce_node_index = nodes.index(sorce_node)
        outbound_edges_count[sorce_node_index] += 1


    sink_nodes = []
    #this loop will look for skinking nodes
    for i in range(len(outbound_edges_count)):
        if outbound_edges_count[i] == 0:
            sink_nodes.append(nodes[i])



    for sink_node in sink_nodes:
        for node in nodes:
            edges.append((sink_node, node))



    N = len(nodes)
    d = 0.85
    epsilon = 0.01

    page_i = array.array('f', [1/N, 1/N, 1/N, 1/N])

    print(page_i)



if __name__ == "__main__":
    main()