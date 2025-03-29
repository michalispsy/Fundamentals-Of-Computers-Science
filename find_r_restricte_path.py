import sys 

class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = self.construct_graph(nodes, init_graph)

    max_weight = 1
    min_weight = sys.maxsize
    
    def construct_graph(self, nodes, init_graph):
        graph = {}

        for node in nodes:
            graph[node] = {}
         
        graph.update(init_graph)
        
        for node, edges in graph.items():
            for adjacent_node, value in edges.items():
                if self.min_weight > value: self.min_weight = value
                if self.max_weight < value: self.max_weight = value
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

def DFS(r, graph, node, end_node, visited):
    
    if node not in visited:
        visited.add(node)
        if node == end_node: return True
        for neighbor in graph.get_outgoing_edges(node):
            if graph.cost(node, neighbor) <= r: DFS(r, graph, neighbor, end_node, visited)
    return end_node in visited
#INPUT the nodes
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
#Input the start and end node and the r
start_node = "A"
end_node = "D"
r = 5

# Function call
if DFS(r, graph, start_node, end_node, set()): print("There is a path from " + start_node + " to " + end_node + " for r=" + str(r))
else : print("There is no path from " + start_node + " to " + end_node + " for r=" + str(r))