

# task 1


def peremini_function():
    x = 1
    y = 2
    str1= "Переміна"

print(peremini_function.__code__.co_nlocals)


# task 2

def function1():
    print ("Hello from outer function")
    def function2():
        print ("Hello from inner function")
    function2()

function1()


class Function:

    def __init__(self):
        self.String1 = "Привіт"
        self.String2 = "Функція"

    def Function2(self):
        print("Function2 : ", self.String1)
        return



class Function_new(Function):

    def Function1(self):
        self.Function2()
        print("Function1 : ", self.String2)
        return

Object1 = Function()

Object2 = Function_new()

Object2.Function1()

# task 3

def choose_func(nums: list, func1, func2):
    pass



nums1 = [1, 2, 3, 4, 5]

nums2 = [1, -2, 3, -4, 5]


def square_nums(nums):
    
    return [num ** 2 for num in nums]


def remove_negatives(nums):

    return [num for num in nums if num > 0]


assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]


