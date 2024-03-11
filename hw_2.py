import random



def get_numbers_ticket(min,max, quantity):
    numbers = []

    if min >= 1 and max <= 1000:


        for i in range(min,max+1):
            numbers.append(i)
        
        numbers = random.sample(numbers, quantity)
        numbers.sort()
        return print(numbers)
    else: 
        print('Введите числа от 1 до 1000')

get_numbers_ticket()   