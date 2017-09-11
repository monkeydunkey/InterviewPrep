'''
Graph representation in python

Dict Rep:
    {
        'Node': [ List of nodes that can be reached ]
    }
'''

graph = {
            'A': ['B', 'C', 'D'],
            'B': ['G'],
            'D': ['E'],
            'E': ['F'],
            'C': ['F']
        }


def naive_path_search(graph, start, end, path=None):
    if path is None:
        path = [start]
    if start == end:
        return path
    else:
        if graph.get(start, None) is None:
            return None
        else:
            for node in graph[start]:
                if node not in path:
                    retpath = naive_path_search(graph, node, end, path + [node])
                    if retpath: return retpath

def depthFirstSearch(graph, start, end):
    seenStates = set()
    stack = list([[start]])
    while len(stack):
        state = stack.pop()
        lastPos = state[-1]
        if lastPos in seenStates:
            continue
        seenStates.add(lastPos)
        if graph.get(lastPos, None) is not None:
            for pos in graph[lastPos]:
                if pos == end:
                    return state + [end]
                else:
                    stack.append(state + [pos])

if __name__ == '__main__':
    print 'Naive path search', naive_path_search(graph, 'A', 'F')
    print 'Depth First Search', depthFirstSearch(graph, 'A', 'F')
