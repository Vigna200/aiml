#Minimax
import math
def minimax(curDepth,nodeIndex,maxTurn,scores,targetDepth):
    if curDepth==targetDepth:
        return scores[nodeIndex]
    if maxTurn:
        return max(minimax(curDepth+1,nodeIndex*2,False,scores,targetDepth),minimax(curDepth+1,nodeIndex*2+1,False,scores,targetDepth))
    else:
        return min(minimax(curDepth+1,nodeIndex*2,True,scores,targetDepth),minimax(curDepth+1,nodeIndex*2+1,True,scores,targetDepth))
scores=[8,15,3,7,10,12,9,5]
treeDepth=int(math.log2(len(scores)))
optimal_value=minimax(0,0,True,scores,treeDepth)
print("The optimal value is:",optimal_value)