import random



def get_numbers_ticket(min,max, quantity):

    numbers = []

    if min >= 1 and max <= 1000:

        if max - min >= quantity:

            for i in range(min,max+1):  
                numbers.append(i)
            
            numbers = random.sample(numbers, quantity)
            numbers.sort()
            return numbers
        
        else: 
            return []
        
    else: 
        return []


get_numbers_ticket(10,14,6)