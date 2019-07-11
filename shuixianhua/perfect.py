for number in range(10000):
    addNum = 0
    for i in range(1,number):
        if number % i == 0:
            addNum += i;
    if addNum == number:
        print(number)