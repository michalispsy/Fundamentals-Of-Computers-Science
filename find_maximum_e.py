class t(object):
    def __init__(self, nodes, init_t):
        self.nodes = nodes
        self.t = self.construct_t(nodes, init_t)
        
    def construct_t(self, nodes, init_t):
        t = {}

        for node in nodes:
            t[node] = {}
         
        t.update(init_t)
        
        for node, edges in t.items():
            for adjacent_node, value in edges.items():
                if t[adjacent_node].get(node, False) == False:
                    t[adjacent_node][node] = value
                    
        return t
    
    def get_nodes(self):
        "Returns the nodes of the t."
        return self.nodes
    
    def get_outgoing_edges(self, node, unvisited_nodes):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            #Το δεύτερο κομμάτι του and statement επιτρέπει μόνο γείτονες που δεν έχουν επισκεφθεί
            if self.t[node].get(out_node, False) != False and out_node in unvisited_nodes:
                connections.append(out_node)
        return connections
    
    def cost(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.t[node1][node2]


def max_e_of_node (t, head_node, Maximum_e, unvisited_nodes):
    
    neighbors = t.get_outgoing_edges(head_node, unvisited_nodes)
    unvisited_nodes.remove(head_node)
    for neighbor in neighbors:
        if Maximum_e[head_node] <= t.cost(head_node, neighbor): e = t.cost(head_node, neighbor)
        else: e = Maximum_e[head_node]

        if e >= Maximum_e[neighbor]: 
            Maximum_e[neighbor] = e
        max_e_of_node(t, neighbor, Maximum_e, unvisited_nodes)
    return Maximum_e

def find_maximums(t):
    
    nodes_of_tree  = list(t.get_nodes())
    Maxs_e = {}
    for node in nodes_of_tree:
        Maxs_e[node] = {}
        for sub_node in nodes_of_tree:
            Maxs_e[node][sub_node] = 0
        Maxs_e[node] = max_e_of_node(t, node, Maxs_e[node], nodes_of_tree.copy())
    return Maxs_e

#Input the nodes
nodes = [ "A", "B", "C", "D", "E", "G", "F", "H", "I"]
init_t = {}
for node in nodes:
    init_t[node] = {}

# μη κατευθυνόμενοι γράφοι
# Input the edges
init_t["A"]["B"] = 7
init_t["B"]["H"] = 9
init_t["A"]["C"] = 3
init_t["C"]["G"] = 8
init_t["C"]["D"] = 4
init_t["C"]["E"] = 2
init_t["E"]["F"] = 5
init_t["D"]["I"] = 1
	
t = t(nodes, init_t)
Minimum_cost = find_maximums(t=t)
for node in nodes:
    print("From " + str(node) + " to: " + str(Minimum_cost[node]))