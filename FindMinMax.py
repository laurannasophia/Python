def findMin(num1, num2):
    minNum = min(num1, num2)
    result = print("Pienempi luku on " + str(minNum))
    return result

def findMax(num1, num2):
    maxNum = max(num1, num2)
    result = print("Suurempi luku on " + str(maxNum))
    return result

num1 = input("Syötä yksi luku ")
num2 = input("Syötä toinen luku ")
num1 = int(num1)
num2 = int(num2)

findMin(num1, num2)
findMax(num1, num2)