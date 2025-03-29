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

def dijkstra_algorithm(k, graph, start_node, end_node):
    unvisited_nodes = list(graph.get_nodes())
 
    Refuels = {}
    GasInTank = {}

    previous_nodes = {}
 
    max_value = sys.maxsize
    for node in unvisited_nodes:
        Refuels[node] = max_value
        GasInTank[node] = max_value

    Refuels[start_node] = 0
    GasInTank[start_node] = k

    while unvisited_nodes:
      
        cur_min_node = None
        for node in unvisited_nodes:
            if cur_min_node == None:
                cur_min_node = node
            elif Refuels[node] < Refuels[cur_min_node]:
                cur_min_node = node
            elif Refuels[node] == Refuels[cur_min_node] and GasInTank[node] > GasInTank[cur_min_node]:
                cur_min_node = node
    
        neighbors = graph.get_outgoing_edges(cur_min_node)
        for neighbor in neighbors:

            temp = GasInTank[cur_min_node] - graph.cost(cur_min_node, neighbor)

            if Refuels[neighbor] == Refuels[cur_min_node] and temp > GasInTank[neighbor]:
                GasInTank[neighbor] = temp
                previous_nodes[neighbor] = cur_min_node

            if Refuels[neighbor] > Refuels[cur_min_node]:
                if temp >= 0:
                    Refuels[neighbor] = Refuels[cur_min_node]
                    GasInTank[neighbor] = temp
                    previous_nodes[neighbor] = cur_min_node
                
                elif Refuels[neighbor] > Refuels[cur_min_node] + 1 and temp < 0:
                    Refuels[neighbor] = Refuels[cur_min_node] + 1
                    GasInTank[neighbor] = k - graph.cost(cur_min_node, neighbor)
                    previous_nodes[neighbor] = cur_min_node
                
                elif Refuels[neighbor] == Refuels[cur_min_node] + 1 and k - graph.cost(cur_min_node, neighbor) > GasInTank[neighbor]:
                    previous_nodes[neighbor] = cur_min_node
                    GasInTank[neighbor] = k - graph.cost(cur_min_node, neighbor)
 
        unvisited_nodes.remove(cur_min_node)
        if cur_min_node == end_node: break
    
    return previous_nodes, GasInTank, Refuels


def print_result(previous_nodes, Refuel, Gas, start_node, target_node):
    path = []
    node = target_node
    
    while node != start_node:
        path.append(node)
        node = previous_nodes[node]
 
    path.append(start_node)
    
    print("We found the following best path with the numbers of refuels {}".format(Refuel[target_node]) + " and the remaining gas is {}." .format(Gas[target_node]))
    print(" -> ".join(reversed(path)))


nodes = ["A", "B", "C", "D", "E", "F", "G"] #input the nodes of the graph
 
init_graph = {}
for node in nodes:
    init_graph[node] = {}

#input the edges of the graph
init_graph["A"]["B"] = 2
init_graph["A"]["C"] = 3
init_graph["A"]["D"] = 4
init_graph["B"]["D"] = 1
init_graph["B"]["G"] = 6
init_graph["B"]["E"] = 5
init_graph["C"]["E"] = 4
init_graph["C"]["F"] = 3
init_graph["D"]["E"] = 4
init_graph["E"]["F"] = 2
init_graph["E"]["G"] = 3
init_graph["F"]["E"] = 1
init_graph["F"]["G"] = 6

#input the vehicle range and the starting and ending nodes
k = 6
start_node = "A"
end_node = "G"

graph = Graph(nodes, init_graph)
previous_nodes, gas, Refuel = dijkstra_algorithm(k, graph=graph, start_node=start_node, end_node=end_node)
print_result(previous_nodes, Refuel, gas,  start_node, end_node)
