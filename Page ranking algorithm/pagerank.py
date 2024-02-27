import array
import heapq

class MaxHeap:
    def __init__(self):
        self.heap = []

    def push(self, value, char):
        heapq.heappush(self.heap, (-value, char))  # Use negative value to simulate max heap

    def pop(self):
        return heapq.heappop(self.heap)[::-1]  # Return tuple with original order

    def peek(self):
        if self.heap:
            return self.heap[0][::-1]
        return None

    def __len__(self):
        return len(self.heap)

    def __str__(self):
        return str([(-value, char) for value, char in self.heap])

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
    #print(outbound_edges_count)



    sink_nodes = []
    #this loop will look for skinking nodes
    for i in range(len(outbound_edges_count)):
        if outbound_edges_count[i] == 0:
            sink_nodes.append(nodes[i])



    for sink_node in sink_nodes:
        for node in nodes:
            edges.append((sink_node, node))

    outbound_edges_count = [0] * len(nodes)
    for edge in edges:
        nodes_with_outgoing_edges.add(edge[0])
        sorce_node = edge[0]
        sorce_node_index = nodes.index(sorce_node)
        outbound_edges_count[sorce_node_index] += 1
    
    #print(outbound_edges_count)



    N = len(nodes)
    d = 0.85
    epsilon = 0.01

    page_rank = MaxHeap()
    val = 1 / len(nodes)  # Calculate the initial PageRank value (1/N)
    # Push initial PageRank value for each node into the MaxHeap
    for node in nodes:
        page_rank.push(val, node)

    #print(page_rank)

    loop_num = 1
    margin_or_error = 1
    while loop_num < 101 and  margin_or_error < epsilon:
        break


if __name__ == "__main__":
    main()
