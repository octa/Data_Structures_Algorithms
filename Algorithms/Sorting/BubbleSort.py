#!/usr/bin/python

"""

Author: Octa
Program that implements Bubble Sort to sort a list of integers.

"""

def bubbleSort(list):
    lengthOfList=len(list)
    for i in range(0,lengthOfList):
        swapped=False
        #print "i = %d"%list[i]
        for j in range(0,lengthOfList-i-1):
            #print "j = %d"%list[j]
            if(list[j]>list[j+1]):
                temp=list[j]
                list[j]=list[j+1]
                list[j+1]=temp
                swapped=True
        #print "\n---------------"
        if not swapped:
            break
    return list

def main():
    list=[5, 8, 3, 1, 2, 7, 6, 4]
    print bubbleSort(list)

if __name__=="__main__":
    main()