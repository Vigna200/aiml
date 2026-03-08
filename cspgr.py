#CSP
def is_consistent(assignment,variable,value,constraints):
    for constraint in constraints:
        if not constraint(assignment,variable,value):
            return False
    return True
def select_unassigned_variable(variables,assignment):
    for variable in variables:
        if variable not in assignment:
            return variable
    return None
def backtrack(assignment,variables,domains,constraints):
    if len(assignment)==len(variables):
        return assignment
    variable=select_unassigned_variable(variables,assignment)
    for value in domains[variable]:
        if is_consistent(assignment,variable,value,constraints):
            assignment[variable]=value
            result=backtrack(assignment,variables,domains,constraints)
            if result is not None:
                return result
            assignment.pop(variable)
    return None
def graph_coloring_constraint(graph):
    def constraint(assignment,variable,value):
        for neighbor in graph[variable]:
            if neighbor in assignment and assignment[neighbor]==value:
                return False
        return True
    return constraint
graph={'A':['B','C'],'B':['A','C','D'],'C':['A','B','D'],'D':['B','C']}
variables=list(graph.keys())
domains={'A':['Red','Green','Blue'],'B':['Red','Green','Blue'],'C':['Red','Green','Blue'],'D':['Red','Green','Blue']}
constraints=[graph_coloring_constraint(graph)]
assignment={}
solution=backtrack(assignment,variables,domains,constraints)
if solution:
    print("Solution found:")
    for node in solution:
        print(node,"->",solution[node])
else:
    print("No solution exists")




