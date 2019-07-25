import csv
import pygal.maps.world
from pygal.maps.world import COUNTRIES

file =  'data_csv.csv'

def get_countries_code(country_name):
    for code, country in COUNTRIES.items():
        if country == country_name:
            return code
    return None



with open(file)  as f:
    pop_data = csv.reader(f)
    countries_data = {}
    for pop in pop_data:
        if pop[2] == '2010':
            country_name = pop[0]
            population = int(pop[3])
            code = get_countries_code(str(country_name))
            if code:
                country_code[code] = population




worldmap_chart = pygal.maps.world.World()
worldmap_chart.title = 'World population in 2010'
worldmap_chart.add('2010 countries', countries_data)

worldmap_chart.render_to_file('world_population.svg')
