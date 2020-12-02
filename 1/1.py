def main():

    input = open("input","r")
    content_list = input.read().splitlines()
  
    print("Part 1:" + str(partOne(content_list)))
  
    print("Part 2:" + str(partTwo(content_list)))

def partOne(content_list):
    length = len(content_list)
    for i in range(length):
        for j in range(1,length):
            if (int(content_list[i]) + int(content_list[j])) == 2020:
                return str(int(content_list[i]) * int(content_list[j]))

def partTwo(content_list):
    length = len(content_list)
    for i in range(length):
        for j in range(1,length):
            for k in range(2,length):  
                if (int(content_list[i]) + int(content_list[j]) + int(content_list[k])) == 2020:
                    return str(int(content_list[i]) * int(content_list[j]) * int(content_list[k]))



if __name__ == "__main__":
    main()