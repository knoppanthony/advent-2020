def main():

    input = open("input","r")
    content_list = input.read().splitlines()
    partOne(content_list)
    partTwo(content_list)

def partTwo(content_list):
    totalValidPasswords = 0
    length = len(content_list)
    for i in range(length):
        #Get Min Range
        min = parseRange(content_list[i],0)

        #Get Max Range
        max = parseRange(content_list[i],1)

        letter = parseLetter(content_list[i])
        password = parsePassword(content_list[i])

        if isValidP2Password(int(min)-1,int(max)-1,letter,password):
            totalValidPasswords += 1

    print("Part Two: " + str(totalValidPasswords))


def isValidP2Password(min,max,letter,password):
    if password[int(min)] == letter and password[int(max)] != letter:
        return True

    if password[int(min)] != letter and password[int(max)] == letter:
        return True

    return False

def partOne(content_list):
    totalValidPasswords = 0
    length = len(content_list)
    for i in range(length):
        #Get Min Range
        min = parseRange(content_list[i],0)

        #Get Max Range
        max = parseRange(content_list[i],1)

        letter = parseLetter(content_list[i])
        password = parsePassword(content_list[i])
        if isValidP1Password(min,max,letter,password):
            totalValidPasswords += 1

    print("Part One: " + str(totalValidPasswords))

def isValidP1Password(min,max,letter,password):
    howManyInstances = password.count(letter)
    if howManyInstances >= int(min) and howManyInstances <= int(max):
        return True


def parseLetter(policyLine):
      return policyLine.split()[1][0]


def parsePassword(policyLine):
     return policyLine.split()[2]

def parseRange(policyLine,minOrMax):

        return policyLine.split()[0].split("-")[minOrMax]



if __name__ == "__main__":
    main()