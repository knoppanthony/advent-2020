from collections import Counter

def main():

    input = open("input", "r")
    answer_list = input.read().split("\n\n")
   
    print(partOne(answer_list))
    print(partTwo(answer_list))


def partTwo(answer_list):
    totalYes = 0
    for answer in answer_list:

        #Count of total people in a group, + 1 because there isn't a newline on the last persons answers.
        groupSize = answer.count('\n')+1
        
        answer = answer.replace('\n', '')
    
        charDict = Counter(answer)

        for key,value in charDict.items():
            if value == groupSize:
                totalYes = totalYes + 1

    return totalYes

def partOne(answer_list):
    totalYes = 0
    for answer in answer_list:
        answer = answer.replace('\n', '')
        
        #set will eliminate duplicate chars
        totalYes =totalYes +  len(set(answer))
    return totalYes

if __name__ == "__main__":
    main()
