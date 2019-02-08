# -*- coding: utf-8 -*-

from csv import writer
from random import randint


def generate_input_in():
    filepath = input("Nom du csv ? ")
    nb_obj = int(input("Combien d'objets doivent être créées ? "))
    delta_weight = int(input("Delta poids ? "))
    delta_value = int(input("Delta valeur ? "))

    generate_input(filepath, nb_obj, delta_weight, delta_value)


def generate_input(filepath, nb_obj, delta_weight, delta_value):
    with open(filepath, 'w') as output:
        csv_output = writer(output, delimiter=';', lineterminator='\n')
        for i in range(nb_obj):
            random_weight = randint(1, delta_weight)
            random_value = randint(1, delta_value)
            if randint(1, 10) < 7:
                random_weight = random_weight + randint(1, 3)/2
            if randint(1, 10) < 3:
                random_value = random_value + randint(1, 5)/2

            csv_output.writerow(['objet_'+str(i), random_weight, random_value])

