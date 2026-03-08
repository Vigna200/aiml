import heapq
def heuristic(state,target):
    return abs(state[0]+state[1]-target)
def astar(j1,j2,target):
    start=(0,0)
    open_list=[]
    heapq.heappush(open_list,(0,start))
    visited=set()
    parent={start:None}
    while open_list:
        f,current=heapq.heappop(open_list)
        if current in visited:
            continue
        visited.add(current)
        x,y=current
        if x==target or y==target:
            path=[]
            while current:
                path.append(current)
                current=parent[current]
            return path[::-1]
        states=[
        (j1,y),
        (x,j2),
        (0,y),
        (x,0),
        (max(0,x-(j2-y)),min(j2,x+y)),
        (min(j1,x+y),max(0,y-(j1-x)))
        ]
        for s in states:
            if s not in visited:
                f=1+heuristic(s,target)
                heapq.heappush(open_list,(f,s))
                if s not in parent:
                    parent[s]=current
j1=int(input("Jug1 capacity: "))
j2=int(input("Jug2 capacity: "))
target=int(input("Target amount: "))
print("Solution:",astar(j1,j2,target))