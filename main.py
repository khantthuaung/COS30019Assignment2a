from graph import Graph
from bfs import bfs
if __name__ == "__main__":
    g = Graph()
    g.loadFile("Map1.txt")

    path, cost = bfs(g)   # your test BFS for now

    print("> Starting Node:", g.start_point)

    if path:
        print("> Destination Node:", path[-1])
        print("> Number of nodes created:", "N/A")  # placeholder for now
        print("> Path:", " -> ".join(map(str, path)))
        print("> Path Cost:", cost)
    else:
        print("> Destination Node:", "N/A")
        print("> Number of nodes created:", "N/A")
        print("> Path: No solution found.")
