import re

def main():

    input = open("input", "r")
    passport_list = input.read().split("\n\n")
    print(partOne(passport_list))
    print(partTwo(passport_list))



def validate_attribute(attribute,value):
    if attribute == "byr":
        if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002:
            return True
    elif attribute == "iyr":
           if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020:
            return True
    elif attribute == "eyr":
         if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030:
            return True
    elif attribute == "hgt":
        hgtLen = len(value)
        if hgtLen > 2:

            if (value[-2:] == "in"):
                num = value[0:hgtLen-2]
                if int(num) >= 59 and int(num) <= 76:
                    return True
            if (value[-2:] == "cm"):
                num = value[0:hgtLen-2]
                if int(num) >= 150 and int(num) <= 193:
                    return True

    elif attribute == "hcl":
        if re.match("#[a-f0-9]{6}$",value):
            return True
    elif attribute == "ecl":
        if value == "amb" or value == "blu" or value == "brn" or value == "gry" or value == "grn" or value == "hzl" or value == "oth":
            return True
    elif attribute == "pid":
        if len(value) == 9 and RepresentsInt(value):
            return True
    elif attribute == "cid":
        return True

    return False

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def partTwo(passport_list):
    validPassportCount = 0
    for passport in passport_list:
        passport_fields = ['byr', 'iyr', 'eyr',
                           'hgt', 'hcl', 'ecl', 'pid', 'cid']

        passport = passport.replace('\n', ' ')
        passport_attributes = passport.split(' ')

        for attribute in passport_attributes:
            if validate_attribute(attribute.split(":")[0],attribute.split(":")[1]):
                passport_fields.remove(attribute.split(":")[0])

            if len(passport_fields) == 0:
                validPassportCount += 1
                break

            if len(passport_fields) == 1:
                if passport_fields[0] == 'cid':
                    validPassportCount += 1
                    break

    return validPassportCount





def partOne(passport_list):
    validPassportCount = 0
    for passport in passport_list:
        passport_fields = ['byr', 'iyr', 'eyr',
                           'hgt', 'hcl', 'ecl', 'pid', 'cid']

        passport = passport.replace('\n', ' ')
        passport_attributes = passport.split(' ')
        print(passport_attributes)
        for attribute in passport_attributes:
            passport_fields.remove(attribute.split(":")[0])

            if len(passport_fields) == 0:
                validPassportCount += 1
                break

            if len(passport_fields) == 1:
                if passport_fields[0] == 'cid':
                    validPassportCount += 1
                    break

    return validPassportCount


if __name__ == "__main__":
    main()
