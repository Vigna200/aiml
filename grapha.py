#A*Graph
import heapq
class Node:
    def __init__(self,name,parent=None):
        self.name=name
        self.parent=parent
        self.g=0
        self.h=0
        self.f=0
    def __lt__(self,other):
        return self.f<other.f
def heuristic(a,b):
    return abs(ord(a)-ord(b))
def add_to_open(open_list,neighbor):
    for node in open_list:
        if node.name==neighbor.name and neighbor.g>node.g:
            return False
    return True
def a_star_graph(graph,start,goal):
    open_list=[]
    closed_set=set()
    start_node=Node(start)
    goal_node=Node(goal)
    heapq.heappush(open_list,start_node)
    while open_list:
        current_node=heapq.heappop(open_list)
        closed_set.add(current_node.name)
        if current_node.name==goal_node.name:
            path=[]
            while current_node:
                path.append(current_node.name)
                current_node=current_node.parent
            return path[::-1]
        for neighbor_name,cost in graph[current_node.name]:
            if neighbor_name in closed_set:
                continue
            neighbor=Node(neighbor_name,current_node)
            neighbor.g=current_node.g+cost
            neighbor.h=heuristic(neighbor_name,goal_node.name)
            neighbor.f=neighbor.g+neighbor.h
            if add_to_open(open_list,neighbor):
                heapq.heappush(open_list,neighbor)
    return None
graph={'A':[('B',1),('C',3)],'B':[('D',1),('E',4)],'C':[('F',2)],'D':[('G',3)],'E':[('G',1)],'F':[('G',5)],'G':[]}
start='A'
goal='G'
path=a_star_graph(graph,start,goal)
print("Path:",path)
