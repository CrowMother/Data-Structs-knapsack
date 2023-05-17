from util import *

#change this to the complex method since this is currently the brute force method
def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w ==0:
                K[i][w] = 0
            
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            
            else:
                K[i][w] = K[i-1][w]
    
    value =  K[n][W]
    currentVal = value
    returnValues = []
    returnValues.append(value)
    for i in range(len(val), -1, -1):
        above = K[i-1][W]
        dif = currentVal - above
        if(currentVal > above):
            if(dif >= val[i-1]):
                
                currentVal = K[i-1][W]
                for j in range(0, len(val)):
                    if(val[j] == dif):
                        returnValues.append(j)
            
    return returnValues


def main():
    print("Knapsack via Dynamic Programming")

    # readin file 
    #first line correspond to number of items and weight of items respectively
    filein = ReadinFile("knapsack.txt")
    
    lineOne = filein[0].split()
    n = int(lineOne[0])
    W = int(lineOne[1])

    val = []
    wt = []
    for i in range(1,n+1):
        line = filein[i].split()
        wt.append(int(line[0]))
        val.append(int(line[1]))  

    startTime = TimeStart()
    K = knapSack(W, wt, val, n)
    total = K.pop(0)
    for i in range(0, len(K)):
        K[i] = K[i] + 1
    print("The optimal Knapsack solution is ", total, " and involves items ", K)

    TimeTotal(startTime)

    


main()