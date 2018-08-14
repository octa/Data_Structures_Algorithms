#!/usr/bin/python

"""

Author: Octa
Program that implements Insertion Sort to sort a list of integers.

"""

def insertionSort(list):

    lengthOfList=len(list)

    for i in range(1, lengthOfList):
        currentElement=list[i]      #assign the current number being compared to a variable to insert into the correct location on the left side of the list.
        currentLocation=i           #this variable is used to scan all the elements on the left side for comparison.
        while(list[currentLocation-1]>currentElement and currentLocation>=1):       #if the current element is lesser than than its previous element, swap.
            list[currentLocation]=list[currentLocation-1]
            currentLocation-=1      #decerement the location to move to the next element on the left side for comparison.
        list[currentLocation]=currentElement        #assign the current element to the correct location when none of the elements on the left side is greater than this.
        print list

    return list

def main():
    list=[5, 1, 3, 8, 2, 7, 6, 4]
    print insertionSort(list)

if __name__=="__main__":
    main()