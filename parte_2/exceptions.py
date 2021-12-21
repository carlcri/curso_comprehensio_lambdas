import random


def main():
    word = ['anitalavalatina', 'burro', 24, 'oso', 313]
    word = random.choice(word)
    print(f'la palabra: {word}')

    try:
        print((lambda cadena: cadena == cadena[::-1])(word))
    except TypeError:
        print(' ERROR solo se pueden ingresar caracteres')
    finally:
        print('Siempre va imprimir esta linea de codigo sin importar hay una excepcion o no')


if __name__=='__main__':
    main()