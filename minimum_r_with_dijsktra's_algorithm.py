import sys
 
class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)
        
    def construct_graph(self, nodes, init_graph):
        graph = {}

        for node in nodes:
            graph[node] = {}
         
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if graph[adjacent_node].get(node, False) == False:
                    graph[adjacent_node][node] = value
                    
        return graph
    
    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes
    
    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) != False:
                connections.append(out_node)
        return connections
    
    def cost(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]

def Minimum_r(graph, start_node, end_node):
    unvisited_nodes = list(graph.get_nodes())
    Minimum_cost = {}
    max_value = sys.maxsize
    
    for node in unvisited_nodes:
        Minimum_cost[node] = max_value  
    Minimum_cost[start_node] = 0
    
    while unvisited_nodes:
        current_min_node = None
        for node in unvisited_nodes: 
            if current_min_node == None:
                current_min_node = node
            elif Minimum_cost[node] < Minimum_cost[current_min_node]:
                current_min_node = node
    
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            
            if Minimum_cost[current_min_node] <= graph.cost(current_min_node, neighbor): comperatable_cost = graph.cost(current_min_node, neighbor)
            else: comperatable_cost = Minimum_cost[current_min_node]

            if comperatable_cost <= Minimum_cost[neighbor]: 
                Minimum_cost[neighbor] = comperatable_cost
       
        unvisited_nodes.remove(current_min_node)
        if current_min_node == end_node: break
    
    return Minimum_cost

nodes = [ "A", "B", "C", "D", "E", "G", "L", "R", "P", "F"]

init_graph = {}
for node in nodes:
    init_graph[node] = {}

# μη κατευθυνόμενοι γράφοι
init_graph["A"]["B"] = 3
init_graph["A"]["G"] = 1
init_graph["B"]["C"] = 5
init_graph["D"]["C"] = 9
init_graph["G"]["B"] = 8
init_graph["G"]["D"] = 9
init_graph["D"]["E"] = 5
init_graph["E"]["C"] = 2

init_graph["G"]["L"] = 7
init_graph["G"]["F"] = 2
init_graph["L"]["D"] = 5
init_graph["L"]["R"] = 3
init_graph["R"]["E"] = 4
init_graph["R"]["P"] = 4
init_graph["P"]["E"] = 2
init_graph["F"]["P"] = 3
	
graph = Graph(nodes, init_graph)

start_node="A"
end_node="D"
Minimum_cost = Minimum_r(graph=graph, start_node=start_node, end_node=end_node)
print("The minimum value of r, for which an r-restricted path between", start_node, "and", end_node, "exists is:", Minimum_cost[end_node])