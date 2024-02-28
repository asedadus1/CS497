class Graph:
    def __init__(self):
        # Initialize the graph with empty sets and dictionaries to be used in other functions
        self.nodes = set()
        self.edges = {}
        self.page_ranks = {}

    def add_edge(self, start_point, end_point):
        # Add an edge that will be used in the main, using start to end points
        self.nodes.add(start_point)
        self.nodes.add(end_point)

        # Use this for a new start point
        if start_point not in self.edges:
            self.edges[start_point] = []
        self.edges[start_point].append(end_point)

    ############# STEP 1 #############
    def handle_sinks(self):
        # used to see any nodes that do not have any edges going to different nodes
        # another condensed version to store the sinks to save space
        sinks = [vertex for vertex in self.nodes if vertex not in self.edges]

        # Connect sinks to all existing nodes
        for sink in sinks:
            for existing_node in self.nodes:
                if existing_node:
                    self.add_edge(sink, existing_node)

        return sinks
    
    def outgoing_links(self, vertex):
        # opposite of sinks, finding nodes that have edges to other nodes
        return self.edges.get(vertex, [])
    
    ############# STEP 3 #############
    def init_page_ranks(self):
        # initialize page ranks 
        n = len(self.nodes)
        init_rank = (1 / n)
        for vertex in self.nodes:
            if vertex in self.edges:
            # assign into the page_ranks dict to store the init_rank
                self.page_ranks[vertex] = init_rank
            # else:
            #     # Assign a small initial value to sinks
            #     self.page_ranks[vertex] = 0.001
    
    ############# STEP 4 #############
    def calculate_page_ranks(self, d, 𝜀):
        n = len(self.nodes)

        # loop through the converging to check the iterations and margin of error
        for _ in range(100):
            prev_ranks = self.page_ranks.copy()

            # loop through the list of nodes
            for vertex in self.nodes:
                incoming_links = [v for v in self.nodes if vertex in self.edges.get(v, [])]
                # equation
                self.page_ranks[vertex] = (1 - d) / n + d * sum(prev_ranks[v] / len(self.edges.get(v, [])) for v in incoming_links)

            # Check convergence
            convergence = all(abs(self.page_ranks[v] - prev_ranks[v]) < 𝜀 for v in self.nodes)
            if convergence:
                print("\nMargin of error < epsilon after iteration", _)
                break

        # Normalize page ranks to ensure they add up to 1
        total_rank_sum = sum(self.page_ranks.values())
        for vertex in self.nodes:
            self.page_ranks[vertex] /= total_rank_sum

    ############# Final Output #############
    def print_final_ranks(self):
        # Print the final ranks based in alphabetical order
        for vertex, rank in sorted(self.page_ranks.items()):
            print(f"Page {vertex}: Rank {rank:.3f}")  

def PageRank(graph):
    # Step 1: Find out sinks, add outgoing links
    sinks = graph.handle_sinks()
    
    # outgoing_links = {vertex: graph.outgoing_links(vertex) for vertex in graph.nodes}
    outgoing_links = {}
    for vertex in graph.nodes:
        outgoing_links[vertex] = graph.outgoing_links(vertex)

    print("################## Sinks ##################\n")
    print(sinks)

    print("\n################## Outgoing Links ##################\n")
    for vertex, links in sorted(outgoing_links.items()):
        print(f"Page {vertex}: {links}")

    # Step 2: Set damping factor (e.g., 𝑑 = 0.85 and 𝜀 = 0.01)
    d = 0.85
    𝜀 = 0.01

    # Step 3: Initialize all ranks to be 1/𝑁
    graph.init_page_ranks()

    # Step 4: Calculate PageRank of each page repetitively based on the equation, converging, as well as total ranks
    graph.calculate_page_ranks(d, 𝜀)

    print("\n################## Final Ranks ##################\n")
    # Print the final ranks
    graph.print_final_ranks()


if __name__ == "__main__":
    graph = Graph()
    # In-class Projects --- Page Rank Algorithm (Slide 11)
    graph.add_edge("C", "A")
    graph.add_edge("D", "A")
    graph.add_edge("B", "A")
    graph.add_edge("B", "C")

    PageRank(graph)
