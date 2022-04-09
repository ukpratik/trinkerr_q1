
def findSteps(num):
    if(num == "1"):
        return 1
    
    if(len(num) == 1 or len(num) == 0):
        return -1

    templist = []
    sum = 0
    steps = 0
    while(1):
        sum = 0
        for i in range(len(num)):
            sum += int(num[i])*int(num[i])
        steps += 1
        if(sum == 1):
            return steps
        num = str(sum)
        if steps > 10000000:
            return -1

if __name__ == '__main__':
    num = input("enter the number : ")
    num = str(num)
    print(findSteps(num))
