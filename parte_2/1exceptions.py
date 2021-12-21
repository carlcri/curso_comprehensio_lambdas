import random

def palindrome(cadena):
    try: 
        if len(cadena)==0:
            raise ValueError('No se debe ingresar una cadena vacia')
        return (lambda cadena: cadena == cadena[::-1])(cadena)
    except ValueError as ve:
        print(ve)
        return False     


def main():
    word = ['anitalavalatina', 'burro', 24, 'oso', 313, ' ', '  ', '   ','']
    word = ['']
    word = random.choice(word)
    print(f'la palabra: {word}')

    try:
        print(palindrome(word))
        print(len(word))
    except TypeError:
        print(' ERROR solo se pueden ingresar caracteres')


if __name__=='__main__':
    main()
