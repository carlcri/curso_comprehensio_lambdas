# Recuerda ejecutar este programa en 3.9 para el ultimo segmento del codigo

from data_workers import DATA

if __name__ == '__main__':

    # Obiene una nueva lista de acuerdo a la condiccion
    python_dev_list = list(filter(lambda worker : worker['language'] == 'python', DATA))
    print(len(python_dev_list))

    # Reutiliza la variable python_dev_list con la funcion map
    python_dev_list = list(map(lambda worker: worker['name'], python_dev_list))
    print(python_dev_list)

    # Obiene una nueva lista de acuerdo a la condiccion, trabaja para Platzi
    work_for_platzi = list(filter(lambda worker: worker['organization'] == 'Platzi', DATA))
    work_for_platzi = list(map(lambda worker: worker['name'], work_for_platzi))

    print(work_for_platzi)

    # Obiene una nueva lista de acuerdo a la condiccion, es mayor de edad
    worker_is_adult = list(filter(lambda worker: worker['age'] > 18, DATA))
    worker_is_adult = list(map(lambda worker: worker['name'], worker_is_adult))

    print(worker_is_adult)

    # crear una nueva lista, cuyos diccionarios tengan cada uno una nueva llave
    old_people = list(map(lambda worker:worker | {'old': worker['age'] > 70}, DATA))
    print(type(old_people))

    for worker in old_people:
        print(worker['name'], worker['old'])





