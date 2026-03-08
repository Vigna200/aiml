#8Puzzle
import heapq
class Puzzle:
    def __init__(self,start_state,goal_state):
        self.start_state=start_state
        self.goal_state=goal_state
        self.n=int(len(start_state)**0.5)
    def manhattan_distance(self,state):
        distance=0
        for index,value in enumerate(state):
            if value!=0:
                goal_index=self.goal_state.index(value)
                current_i,current_j=divmod(index,self.n)
                goal_i,goal_j=divmod(goal_index,self.n)
                distance+=abs(goal_i-current_i)+abs(goal_j-current_j)
        return distance
    def get_neighbors(self,state):
        neighbors=[]
        zero_index=state.index(0)
        i,j=divmod(zero_index,self.n)
        directions=[(-1,0),(1,0),(0,-1),(0,1)]
        for di,dj in directions:
            new_i=i+di
            new_j=j+dj
            if 0<=new_i<self.n and 0<=new_j<self.n:
                new_index=new_i*self.n+new_j
                new_state=state[:]
                new_state[zero_index],new_state[new_index]=new_state[new_index],new_state[zero_index]
                neighbors.append(new_state)
        return neighbors
    def solve(self):
        start_state=tuple(self.start_state)
        goal_state=tuple(self.goal_state)
        frontier=[]
        heapq.heappush(frontier,(self.manhattan_distance(start_state),0,start_state,[]))
        explored=set()
        while frontier:
            _,g,current_state,path=heapq.heappop(frontier)
            if current_state==goal_state:
                return path
            explored.add(current_state)
            for neighbor in self.get_neighbors(list(current_state)):
                neighbor_tuple=tuple(neighbor)
                if neighbor_tuple not in explored:
                    f=g+1+self.manhattan_distance(neighbor_tuple)
                    heapq.heappush(frontier,(f,g+1,neighbor_tuple,path+[neighbor_tuple]))
        return None
start=[1,2,3,4,5,6,7,0,8]
goal=[1,2,3,4,5,6,7,8,0]
puzzle=Puzzle(start,goal)
solution_path=puzzle.solve()
if solution_path:
    for step in solution_path:
        print(step)
else:
    print("No solution found")
