import random



def get_numbers_ticket(min,max, quantity):
    numbers = []

    if min >= 1 and max <= 1000:


        for i in range(min,max+1):
            numbers.append(i)
        
        numbers = random.sample(numbers, quantity)
        numbers.sort()
        return numbers
    
    else: 
        numbers = []
        return numbers

get_numbers_ticket(0,10,5)