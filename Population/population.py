import csv
import pygal.maps.world
from pygal.maps.world import COUNTRIES
from pygal.style import RotateStyle

file =  'Population/data_csv.csv'

def get_countries_code(country_name):
    '''находит код страны по ее названию'''
    for code, country in COUNTRIES.items():
        if country == country_name:
            return code
    return None



with open(file)  as f:
    pop_data = csv.reader(f)
    #построение словаря с данными о коде страны и численности населения.
    countries_data = {}
    for pop in pop_data:
        if pop[2] == '2010':
            country_name = pop[0]
            population = int(pop[3])
            code = get_countries_code(str(country_name))
            if code:
                countries_data[code] = population

    # группировка стран по численности
    cc_pops_1, cc_pops_2, cc_pops_3, cc_pops_4 = {}, {}, {}, {}
    for cc, pop in  countries_data.items():
        if pop < 1000000:
            cc_pops_1[cc] = pop
        elif pop < 100000000:
            cc_pops_2[cc] = pop
        elif pop < 1000000000:
            cc_pops_3[cc] = pop
        else:
            cc_pops_4[cc] = pop

    #number of countries
    num_counr_1, num_counr_2, num_counr_3, num_counr_4 = str(len(cc_pops_1)), str(len(cc_pops_2)), str(len(cc_pops_3)), str(len(cc_pops_4))

wm_style = RotateStyle('#336699')
worldmap = pygal.maps.world.World(style=wm_style)
worldmap.title = 'World population in 2010'

worldmap.add('0-10m ' + num_counr_1 , cc_pops_1 )
worldmap.add('10-100m ' + num_counr_2, cc_pops_2 )
worldmap.add('100-1bn ' + num_counr_3, cc_pops_3 )
worldmap.add('>1bn ' + num_counr_4, cc_pops_4 )

worldmap.render_to_file('Population/world_population.svg')
