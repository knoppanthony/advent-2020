from collections import Counter

def main():

    input = open("input", "r")
    instruction_list = input.read().splitlines()
   
    partOne(instruction_list)
    partTwo(instruction_list)

#Brute force...change every instruction...see if we loop.
def partTwo(instruction_list):
    accumulator = 0
    i = 0 
    modInstructionIndex=  0

    
    while modInstructionIndex < len(instruction_list):
        print(modInstructionIndex)
        accumulator = 0
        i = 0
        seenInstructions = []
        while i < len(instruction_list):
            ins,amount = instruction_list[i].strip().split(" ")

            if i in seenInstructions:
                print("repeat at accum:" + str(accumulator))
                modInstructionIndex += 1
                break

            seenInstructions.append(i)

            if modInstructionIndex == i:
                if ins == "jmp":
                    ins = "nop"
                elif ins == "nop":
                    ins = "jmp"
                else:
                    ins = ins

            if ins == "acc":
                accumulator += int(amount)
                i += 1
            elif ins == "jmp":
                i += + int(amount)
            elif ins == "nop":
                i += 1
            else:
                print("EOF or we did something wrong")

            if i == len(instruction_list) - 1 and ins != "jmp":
                print("AccumWeDidIt:" + str(accumulator))
                break



def partOne(instruction_list):
    accumulator = 0
    i = 0 
    seenInstructions = []
    while i < len(instruction_list):
        ins,amount = instruction_list[i].strip().split(" ")

        if i in seenInstructions:
            print(accumulator)
            break

        seenInstructions.append(i)

        if ins == "acc":
            accumulator += int(amount)
            i += 1
        elif ins == "jmp":
            i += + int(amount)
        elif ins == "nop":
            i += 1
        else:
            print("EOF or we did something wrong")
        print(ins + " " + amount + " " + str(i))

if __name__ == "__main__":
    main()
