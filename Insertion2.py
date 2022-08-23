#Insertion Sort: 
#Conventional way
#a given list is sorted applying the insertion sort way

import random
def insercion(randomlist):
    for i in range(1,len(randomlist)):
        actual = randomlist[i]
        index=i 
        while index > 0 and randomlist[index-1] > actual:
            randomlist[index] = randomlist[index-1]
            index = index -1
        randomlist[index] = actual
    return randomlist
    



if __name__=="__main__":

    randomlist = [random.randint(1,100) for i in range (5)]
    print(randomlist)
    print(insercion(randomlist))
