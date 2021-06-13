def DFS_help(graph, v, visited):
    visited[v] = True
    successors = graph.get_successors(v)
    for i in successors:
        if not visited[i]:
            DFS_help(graph, i, visited)


def connected(graph):
    n = graph.get_order()
    visited = [False] * n
    for i in range(n):
        if len(graph.get_successors(i)) > 1:
            break
    if i == n - 1:
        return True
    DFS_help(graph, i, visited)
    for i in range(n):
        if not visited[i] and len(graph.get_successors(i)) > 0:
            return False
    return True


def euler_circuit(graph):
    if not connected(graph):
        return False
    else:
        for i in range(graph.get_order()):
            if len(graph.get_successors(i)) % 2 != 0:
                return False
        return True
