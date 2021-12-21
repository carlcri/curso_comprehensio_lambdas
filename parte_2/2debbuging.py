import random


def divisors(number):
    try:
        if number < 0:
            raise ValueError('el numero es negativo zoquete')
        divisors = [i for i in range(1,number+1) if number%i == 0]
        return divisors
    except ValueError as va:
        print(va)
        exit()
   
    
def run():

    numbers = [i for i in range(100)]

    number = new_func(numbers)

    my_divisors = divisors(number)

    print(f'The divisors of {number} are {my_divisors}')
    print('El programa ha terminado')

#Funcion de ingreso de datos aleatorios o de usuario
def new_func(numbers):
    pizza = list('pizza es la mejor comida del mundo y de toda Italia, Espana, y Belgica')
    sign = [-1, 1]
    sign = random.choice(sign)

    numbers = numbers + pizza
    number = random.choice(numbers)

    try:
        if isinstance(number,int):
            return number*sign
        else:
            raise TypeError('solo se pueden ingresar numeros gran cabron')   
    except TypeError as ve:
        print(ve)
        exit()          

 
if __name__ == '__main__':
    run()