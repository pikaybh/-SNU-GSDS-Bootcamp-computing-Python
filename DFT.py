# %%
from collections import deque

# %%
class undi_graph():
    def __init__(self, V: list, E: list) -> None:
        self.V = V[: ]
        self.neighbor = {}

        for v in V:
            self.neighbor[v] = []

        for (v, w) in E:
            self.neighbor[v].append(w)
            self.neighbor[w].append(v)

    def __DFTHelp(self, visited: list, v: int) -> None:
        if not visited[v]:
            # Do something only when the vertex is not visited!
            visited[v] = True

            # Pre order
            print("Pre-", v, end=("\n" if v == 3 else ", "))

            # Visit all the neighbors
            for w in self.neighbor[v]:
                self.__DFTHelp(visited, w)
                
            # Post order (action after visiting all the neighbors)    
            print("Post-", v, end=("\n" if v == 2 else ", "))

    def DFT(self) -> None:
        if self.V:
            # Initialization
            visited = {}
            
            for v in self.V:
                visited[v] = False

            # Traversal - "for loop" is necessary to visit all disconnected noeds
            for v in self.V:
                self.__DFTHelp(visited, v)

    def BFT(self) -> None:
        if self.V:
            # Initialization
            visited ={}

            for v in self.V:
                visited[v] = False

            q = deque([])

            # Traversal
            for v in self.V:
                q.append(v)
                
                while q:
                    # Get the first vertex!
                    v = q.popleft()

                    if not visited[v]:
                        # Do something when it is not visited
                        visited[v] = True
                        print(v)

                        # Visit all the neighbors
                        for w in self.neighbor[v]:
                            q.append(w)

                        print(q)


if __name__ == "__main__":
    V = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    E = [(0, 1), (1, 4), (4, 6), (6, 9), (6, 5), (5, 1), (5, 7), (7, 8), (2, 3)]
    graph = undi_graph(V, E)
    graph.DFT()
    graph.BFT()





# %%
