class Graph:
    def __init__(self, vertices):
        self.V = vertices  # Number of vertices
        self.graph = []  # List to store edges: [weight, u, v]

    # Add an edge to the graph
    def add_edge(self, u, v, w):
        self.graph.append([w, u, v])

    # Find the parent of a node
    def find_parent(self, parent, i):
        if parent[i] == i:
            return i
        return self.find_parent(parent, parent[i])

    # Perform union of two subsets
    def union(self, parent, rank, x, y):
        root_x = self.find_parent(parent, x)
        root_y = self.find_parent(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Kruskal's algorithm to find Minimum Spanning Tree
    def kruskal_mst(self):
        self.graph.sort()  # Sort edges by weight
        parent = []
        rank = []
        result = []  # Store the MST edges

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        e = 0  # Number of edges in MST
        i = 0  # Index for sorted edges

        while e < self.V - 1:
            w, u, v = self.graph[i]
            i += 1
            root_u = self.find_parent(parent, u)
            root_v = self.find_parent(parent, v)

            if root_u != root_v:
                result.append([u, v, w])
                self.union(parent, rank, root_u, root_v)
                e += 1

        # Print the edges of the MST
        print("Edges in the Minimum Spanning Tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")

# Test Kruskal's Algorithm
if __name__ == "__main__":
    g = Graph(4)
    g.add_edge(0, 1, 10)
    g.add_edge(0, 2, 6)
    g.add_edge(0, 3, 5)
    g.add_edge(1, 3, 15)
    g.add_edge(2, 3, 4)

    g.kruskal_mst()