# Instructions:
# This is a group in-class project (1-2 students in a team, please 
# signup in People->Page Rank Algorithm first before submission). 
# The detailed project instructions are given during class and 
# can also be found in our slides for Google's PageRank algorithm.
# Implement Page Rank Algorithm for the following structure. 
# Include a screenshot of your code (You can implement the program 
# in any language of your choice (Python, C/C++, etc.), and 
# provide the final ranks for each page (node).

# Keep in mind:
# Implement Page Rank Algorithm for the following structure.
# Provide the final ranks for each page (node)

# Equation: xi = (1-d)/n + d * (sum of j in i)(xj/|out(j)|)
# 𝑑: damping factor
# N: total number of pages
# 𝑖𝑛(𝑖): the set of pages that link to page 𝑖
# |𝑜𝑢𝑡(𝑗)| : the number of outbound links on page 𝑗 PageRank Formulation

# import numpy as np

class Graph:
    def __init__(self):
        self.vertices = set()
        self.edges = {}
        self.page_ranks = {}

    def add_edge(self, start_point, end_point):
        self.vertices.add(start_point)
        self.vertices.add(end_point)

        if start_point not in self.edges:
            self.edges[start_point] = []
        self.edges[start_point].append(end_point)

    def find_sinks(self):
        sinks = [vertex for vertex in self.vertices if vertex not in self.edges]
        return sinks
    
    def outgoing_links(self, vertex):
        return self.edges.get(vertex, [])

    # def init_page_ranks(self):
    #     n = len(self.vertices)
    #     init_rank = 1/n
    #     for vertex in self.vertices:
    #         self.page_ranks[vertex] = init_rank
    
    

def PageRank(graph):
    # Step 1: Find out sinks, add outgoing links
    sinks = graph.find_sinks()
    outgoing_links = {vertex: graph.outgoing_links(vertex) for vertex in graph.vertices}
    print(f"Sinks: {sinks}")
    print("Outgoing Links: ")
    for vertex, links in outgoing_links.items():
        print(f"Page {vertex}: {links}")

    # Step 2: Set damping factor (e.g., 𝑑 = 0.85 and 𝜀 = 0.01)
    d = 0.85
    epsilon = 0.01

    # Step 3: Initialize all ranks to be 1/𝑁
    n = len(graph.vertices)
    init_rank = 1/n
    for vertex in graph.vertices:
        if vertex in graph.edges:
            graph.page_ranks[vertex] = init_rank
        else:
            # Assign a small initial value to sinks
            graph.page_ranks[vertex] = 0.001

    # Step 4: Calculate PageRank of each page repetitively based on the equation
    for _ in range(100):
        prev_ranks = graph.page_ranks.copy()

        for vertex in graph.vertices:
            incoming_links = [v for v in graph.vertices if vertex in graph.edges.get(v, [])]
            graph.page_ranks[vertex] = (1 - d) / n + d * sum(prev_ranks[v] / len(graph.edges.get(v, [])) for v in incoming_links)

        # Check convergence
        convergence = all(abs(graph.page_ranks[v] - prev_ranks[v]) < epsilon for v in graph.vertices)
        if convergence:
            break

    # Normalize page ranks to ensure they add up to 1
    total_rank_sum = sum(graph.page_ranks.values())
    for vertex in graph.vertices:
        graph.page_ranks[vertex] /= total_rank_sum

    # Print the final ranks
    for vertex, rank in sorted(graph.page_ranks.items(), key=lambda x: x[1], reverse=True):
        print(f"Page {vertex}: Rank {rank:.4f}")

    
    # ❖ What data structures and variables you need to store your ranks and vertices?
    # ❖ All PageRanks should add up to 1.
    # ❖ Pages with more links should have higher pageranks than pages with fewer
    # links.
    # ❖ Sinks should not have a pagerank of 0.
    # ❖ First make sure your algorithm works on small, simple graphs , and then test
    # it on a large graph.


    # print("Hello")

if __name__ == "__main__":
    graph = Graph()
    graph.add_edge("C", "A")
    graph.add_edge("D", "A")
    graph.add_edge("B", "A")
    graph.add_edge("B", "C")
    PageRank(graph)