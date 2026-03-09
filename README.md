"# aiml" 
def is_safe(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack(assignment, graph, colors):
    if len(assignment) == len(graph):
        return assignment
    for node in graph:
        if node not in assignment:
            for color in colors:
                if is_safe(node, color, assignment, graph):
                    assignment[node] = color
                    result = backtrack(assignment, graph, colors)
                    if result:
                        return result
                    del assignment[node]
            return None
graph = {
'A':['B','C'],
'B':['A'],
'C':['A']
}
colors = ['Red','Green']
solution = backtrack({}, graph, colors)
print("Solution:", solution)
