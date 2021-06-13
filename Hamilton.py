def is_path(graph, v, pos, path):
    if graph.is_edge(path[pos - 1], v) == 0:
        return False
    if v in path:
        return False
    return True


def hamilton_cycle_help(graph, path, pos):
    n = graph.get_order()
    if pos == n:
        if graph.is_edge(path[pos - 1], path[0]) == 1:
            return True
        else:
            return False
    for v in range(1, n):
        if is_path(graph, v, pos, path):
            path[pos] = v
            if hamilton_cycle_help(graph, path, pos + 1):
                return True
            path[pos] = -1
    return False


def hamilton_cycle(graph):
    path = [-1] * graph.get_order()
    path[0] = 0
    if not hamilton_cycle_help(graph, path, 1):
        return False
    return True
