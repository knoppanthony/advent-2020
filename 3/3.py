
import numpy as np
def main():

  tMap = np.loadtxt("input",delimiter="/n",dtype="str",comments="a")
  
  numTrees = partOne(tMap)
  print("Part One: " + str(numTrees))

  numTrees = partTwo(tMap,1,1) *  partTwo(tMap,3,1) *  partTwo(tMap,5,1) *  partTwo(tMap,7,1) *  partTwo(tMap,1,2)
  print ("Part Two: "+ str(numTrees))




def partTwo(tMap,howManyColumns,howManyRows):

    numRows = len(tMap)-1
    numCols = len(tMap[0])-1
    row = howManyRows
    col = howManyColumns
    numTrees = 0
    while (row <= numRows):
   
        if tMap[row][col] == '#':
            numTrees += 1

        row += howManyRows
        col += howManyColumns

        if col > numCols:
            col = abs(len(tMap[0]) - col)
     
        
    return numTrees

def partOne(tMap):
    #follow the slope of R3 D1 how many trees?
    numRows = len(tMap)-1
    numCols = len(tMap[0])-1
    row = 1
    col = 3
    numTrees = 0
    while (row <= numRows):
   
        if tMap[row][col] == '#':
            numTrees += 1

        row += 1
        col += 3

        if col > numCols:
            col = abs(len(tMap[0]) - col)
     
        
    return numTrees
if __name__ == "__main__":
    main()