import math
trainDetails = {"dist":0,"perCap":30,"no":6,"loaded":0}
minePoints = {1:[50,50],2:[25,100],3:[140,200],4:[80,300],5:[200,60]}
# routeMap = [[1,1,1,1,1],
#             [1,0,1,0,1]
#             [1,1,0,1,0]
#             [1,0,1,0,1]
#             [1,1,0,1,0]]
routeMap = {0:[1,2,3,4,5],1:[2,3,4,5],2:[1,3,5],3:[1,2,4],4:[1,3,5],5:[1,2,4]}

class CostGenrator:
    def __init__(self,perCap,no,loaded):
        self.perCap = perCap
        self.no = no
        self.loaded = loaded
    
    def getWagLoadVal(self,coalProdCap,maxCap):
        if self.loaded+coalProdCap<=maxCap:
            return coalProdCap
        else:
            return maxCap-self.loaded
        
    def generateCost(self):
        finalRoute = []
        totalCost = 0
        initialCap = 0
        maxCap = self.perCap*self.no
        currPos = 0
        ctr = 0
        while initialCap!=maxCap:
            selPoint = -1
            selCost = -1
            for x in routeMap[currPos]:
                if x not in finalRoute:
                    distCost = math.floor(((self.loaded/maxCap)*100)+minePoints[x][0])
                    wagCost = math.floor(100-((self.loaded+self.getWagLoadVal(minePoints[x][1],maxCap))/maxCap)*100)
                    total = distCost+wagCost
                    if(selCost<0):
                        selCost = total
                        selPoint = x
                    else:
                        if total<selCost:
                            selCost = total
                            selPoint = x
            ctr+=1
            currPos = selPoint
            self.loaded = self.getWagLoadVal(minePoints[selPoint][1],maxCap)
            initialCap+=self.getWagLoadVal(minePoints[selPoint][1],maxCap)
            totalCost+=selCost
            finalRoute.append(selPoint)
        return finalRoute,totalCost

# route,totalCost = CostGenrator(30,6,0).generateCost()
# print(route,totalCost)


                
                
