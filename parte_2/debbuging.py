import random


def divisors(number):
    divisors = [i for i in range(1,number+1) if number%i == 0]
    return divisors

def run():

    numbers = [i for i in range(100)]

    number = random.choice(numbers)
    my_divisors = divisors(number)

    print(f'The divisors of {number} are {my_divisors}')


    

if __name__ == '__main__':
    run()