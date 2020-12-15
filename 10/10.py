
from collections import defaultdict 
def main():

    input = open("input", "r")
    out_jolt_list = input.readlines()
    out_jolt_list = [int(i) for i in out_jolt_list]

    partOne(out_jolt_list)
    partTwo(out_jolt_list)

#I STOLE THIS - 
def partTwo(out_jolt_list):

    # paths[n] is the total paths from 0 to n
    paths = defaultdict(int)
    paths[0] = 1

    for adapter in sorted(out_jolt_list):
        for diff in range(1, 4):
            next_adapter = adapter + diff
            if next_adapter in out_jolt_list:
                paths[next_adapter] += paths[adapter]
    print(paths)

def partOne(out_jolt_list):
    out_jolt_list.sort()
    print(out_jolt_list)
    oneJumps = 0
    threeJumps = 0
    for i in range(0,len(out_jolt_list)):

        #need the outlet
        if i == 0:
            if out_jolt_list[i] == 1:
                oneJumps += 1
            if out_jolt_list[i] == 3:
                oneJumps += 3
            if out_jolt_list == 2:
                print("WTF")

        if i == len(out_jolt_list)-1:
            jumpSize = 3
        else:
            jumpSize = out_jolt_list[i+1] - out_jolt_list[i]

        if jumpSize == 1:
            oneJumps += 1
        elif jumpSize == 3:
            threeJumps +=1
        else:
            print("WTF")

        print(out_jolt_list[i])
    print(str(oneJumps))
    print(str(threeJumps))


if __name__ == "__main__":
    main()
