
# normal method
def summation(x,n):
    result = 0
    for i in range(1,n+1):
        expresult = 1/(x ** i)
        result += expresult
    return result

print(summation(10,5))



# Another method to find summation

def sum_recursion(x,n):
    result = []
    for i in range(1, n + 1):
        expresult = 1 / (x ** i)
        result .append(expresult)

    # using recursion to add elements in list

    def listsum(numList):
        if len(numList) == 1:
            return numList[0]
        else:
            return numList[0] + listsum(numList[1:])

    final_result = listsum(result)
    return final_result


print(sum_recursion(10,5))





