from multiprocessing.connection import wait
import time

def ReadinFile(fileChoice): 
    list = []
    with open(fileChoice, 'r') as file:
        for line in file:
            list.append(line)
        file.close()
    return list

def TimeStart():
    return(time.time())

def TimeTotal(startTime):
    print("Total time: ", (time.time() - startTime))


