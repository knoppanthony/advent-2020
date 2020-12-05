
import numpy as np
def main():

    with open("input") as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content] 

    print(partOne(content))
    print(partTwo(content))



    
def partTwo(content):
    highestSeatId = 0
    seats = []
    for seat in content:
        lower_boundRow = 0
        upper_boundRow = 127
        lower_boundCol = 0
        upper_boundCol = 7

        for command in seat:
            if command == 'F':
                upper_boundRow = (upper_boundRow + lower_boundRow) // 2
            if command == 'B':
                lower_boundRow = (upper_boundRow + lower_boundRow) // 2 + 1

            if command == 'L':
                upper_boundCol = (upper_boundCol + lower_boundCol) // 2
            if command == 'R':
                lower_boundCol = (upper_boundCol + lower_boundCol) // 2 + 1

        currentSeatId = (lower_boundRow * 8) + lower_boundCol 
        #print(seat)
        #print("Seat:" + str(lower_boundRow) )
        #print("Col:" + str(lower_boundCol) )
        #print(currentSeatId)
        seats.append(currentSeatId)
        if currentSeatId > highestSeatId:
            highestSeatId = currentSeatId
    seats.sort()

    # look for a gap in the sorted list of seatID's
    for i in range(len(seats)):
        if i == len(seats)-1:
            break

        if seats[i+1] - seats[i] != 1:
            return seats[i] + 1
    
     

def partOne(content):
    highestSeatId = 0
    for seat in content:
        lower_boundRow = 0
        upper_boundRow = 127
        lower_boundCol = 0
        upper_boundCol = 7

        for command in seat:
            if command == 'F':
                upper_boundRow = (upper_boundRow + lower_boundRow) // 2
            if command == 'B':
                lower_boundRow = (upper_boundRow + lower_boundRow) // 2 + 1

            if command == 'L':
                upper_boundCol = (upper_boundCol + lower_boundCol) // 2
            if command == 'R':
                lower_boundCol = (upper_boundCol + lower_boundCol) // 2 + 1

        currentSeatId = (lower_boundRow * 8) + lower_boundCol 
        #print(seat)
        #print("Seat:" + str(lower_boundRow) )
        #print("Col:" + str(lower_boundCol) )
        #print(currentSeatId)
        if currentSeatId > highestSeatId:
            highestSeatId = currentSeatId
    return highestSeatId
     


 
if __name__ == "__main__":
    main()