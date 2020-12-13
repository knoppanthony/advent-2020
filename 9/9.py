from collections import Counter

def main():

    input = open("input", "r")
    xmas_numbers = input.read().splitlines()
   
    partOne(xmas_numbers)
    partTwo(xmas_numbers)

def partTwo(xmas_numbers):
    numToFind = 26796446
    startIndex = 0
    currentIndex = 0
    smallestNum = 0
    largestNum = 0
    currentSum = 0

    while startIndex < len(xmas_numbers):
        smallestNum = int(xmas_numbers[currentIndex])
        while currentSum < numToFind:
            currentValue = int(xmas_numbers[currentIndex])
            #Annoying
            if currentValue < smallestNum:
                smallestNum = currentValue

            if currentValue > largestNum:
                largestNum = currentValue

    
            currentSum += currentValue
            if currentSum == numToFind:
                print("Found! Small: " + str(smallestNum) )
                print("Big: " + str(largestNum))
                print("Answer:" + str(smallestNum + int(largestNum)))
            currentIndex += 1
        
        startIndex += 1
        currentSum = 0
        currentIndex = startIndex
        smallestNum = 0
        largestNum = 0

        



def partOne(xmas_numbers):
    preamble_length = 25
    s = set()
     
    for i in range(preamble_length,len(xmas_numbers)):
        flag = False
        s = set()
        #first loop through and build the set for the current window
        for j in range(i-preamble_length, i):
            if int(xmas_numbers[i]) - int(xmas_numbers[j]) in s:
                flag = True
            s.add(int(xmas_numbers[j]))
        
        if flag == False:
            print("No sum found for: " + str(xmas_numbers[i]) )
        

if __name__ == "__main__":
    main()
