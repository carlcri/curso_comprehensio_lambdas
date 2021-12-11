
def main():
    # Cuadrado de los numeros del 1 al 100. que no sean divisibles por 3
    squares = [i**1 for i in range(100) if i%3 != 0 ]
    print(squares)


if __name__ == '__main__':
    main()
