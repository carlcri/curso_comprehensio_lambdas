
def main():

    my_list = [1, 'pedro', True, 2.0]
    my_dict = {"firstname":'Benito', "lastname":"ochoa"}

    super_list = [
        my_dict,
        {"firstname":'Andres', "lastname":"Berenche"},
        {"firstname":'Alonso', "lastname":"Cabrera"}
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, -3, 8],
        "floating_nums": [1.1, 2.3, 4.2]
    }

    print(type(my_list))
    print(type(my_dict))
    print(type(super_dict))
    print(super_list)
    print(super_dict)


if __name__ == '__main__':
    main()
