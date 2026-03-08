#AlphaBetaPruning
import math
MAX=1000
MIN=-1000
def minimax(depth,nodeIndex,maximizingPlayer,values,alpha,beta):
    if depth==int(math.log2(len(values))):
        return values[nodeIndex]
    if maximizingPlayer:
        best=MIN
        for i in range(2):
            val=minimax(depth+1,nodeIndex*2+i,False,values,alpha,beta)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=MAX
        for i in range(2):
            val=minimax(depth+1,nodeIndex*2+i,True,values,alpha,beta)
            best=min(best,val)
            beta=min(beta,best)
            if beta<=alpha:
                break
        return best
values=[4,2,6,8,1,9,3,7]
print("The optimal value is :",minimax(0,0,True,values,MIN,MAX))