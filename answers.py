print("------------------- Question 1 ----------------")
print("The function isIncreasing loops through the list of nums and checks to see if nums[i] is greater than nums[i-1]. This is done in order to check that the list of nums increases continouslly, if so returns True. If it does not, it returns False.")

def isIncreasing(nums):
    next = nums[0]
    for i in range(len(nums)):
        if nums[i] >= next:
            next = nums[i]
        elif nums[i] < next:
            return False
        else:
            return False

    return True

print(isIncreasing([1,2,3,4,0]))

print("------------------- Question 2 ----------------")
print("This function loops through the list of nums and adds the converted str and adds it to the variable final. After loopign through all the nums in the list it return the an integer.")

def NumConvert(nums):
    final = "";
    for i in range(len(nums)):
        final = final + str(nums[i])
    return int(final)

print(NumConvert([1,2,3,4]))
# print(NumConvert([2,3,4,5,6,7]))


print("------------------- Question 3 ----------------")
print("This function loops in reverse order our binary string to a decimal. If it sees a 0 our deci is count + 3")

def BinConvert(bin):
    reversed = ''
    for char in bin:
        reversed = char + " " + reversed
    count = 0;
    a = reversed.split(" ")
    a1 = a[:-1]
    print(a1, "str split into a list")
    print()
    for i in range(len(a1)):
        if a1[i] == "0":
            count = count + 1
            if a1[(i+1)] == 1:
                count = count + 2
            if a1[(i+1)] == 0:
                count = count + 1
        elif a1[i] == "1":
            count = count + 2
            if a1[(i+1)]  == 0:
                count = count + 1
            if a1[(i+1)] == 1:
                count = count + 2
    return count
    
print(BinConvert("100"))