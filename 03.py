import heapq

class Solution:
    def spanningTree(self, V, adj):
        pq = [(0, 0)]  # (wt, node)
        vis = [0] * V
        total_weight = 0

        while pq:
            wt, node = heapq.heappop(pq)

            if vis[node] == 1:
                continue

            vis[node] = 1
            total_weight += wt

            for adjNode, edgWt in adj[node]:
                if not vis[adjNode]:
                    heapq.heappush(pq, (edgWt, adjNode))

        return total_weight

if __name__ == "__main__":
    V = int(input("Enter the number of vertices: "))
    adj = [[] for _ in range(V)]

    E = int(input("Enter the number of edges: "))
    print("Enter the edges in the format (source, destination, weight):")
    for _ in range(E):
        u, v, wt = map(int, input().split())
        adj[u].append((v, wt))
        adj[v].append((u, wt))  # Assuming undirected graph

    obj = Solution()
    min_spanning_tree_weight = obj.spanningTree(V, adj)
    print("Sum of weights of edges of the Minimum Spanning Tree:", min_spanning_tree_weight)
