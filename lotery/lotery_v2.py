import random
number = []
numbers = []
def get_numbers():

    ten = [1, 1, 1, 2, 2, 2, 2, 2, 2]
    number1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    number2 = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    number3 = [20, 21, 22, 23, 24, 25, 26, 27, 28, 29]
    number4 = [30, 31, 32, 33, 34, 35, 36, 37, 38, 39]
    number5 = [40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
    number6 = [50, 51, 52, 53, 54, 55, 56, 57, 58, 59]
    number7 = [60, 61, 62, 63, 64, 65, 66, 67, 68, 69]
    number8 = [70, 71, 72, 73, 74, 75, 76, 77, 78, 79]
    number9 = [80, 81, 82, 83, 84, 85, 86, 87, 88, 89]
    name = [number1, number2,number3,number4, number5, number6, number7, number8, number9]
    random.shuffle(ten)

    a = 0
    for i in ten:
        number.append(random.sample(name[a],i))
        a+= 1

    a = 0
    for i in number:

        for i in number[a]:
            numbers.append(i)
        a += 1





    
    
