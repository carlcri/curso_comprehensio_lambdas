import random


def divisors(number):
    divisors = [i for i in range(1,number+1) if number%i == 0]
    return divisors

def run():

    numbers = [i for i in range(100)]

    number = new_func(numbers)
    #input('pausa')
    my_divisors = divisors(number)

    print(f'The divisors of {number} are {my_divisors}')
    print('El programa ha terminado')

def new_func(numbers):
    number = random.choice(numbers)
    return number
 
if __name__ == '__main__':
    run()