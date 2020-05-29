import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone_project.settings')

import django
django.setup()

## POPULATION script
from capstone_app.models import City, Salary
import salary_web_scraper as web_scrape

import urllib.request
import json
import requests


def populate():

    city_actual = {'Ann Arbor': 0.942 , 'Atlanta':1.025, 'Austin':0.925, 'Baltimore':1.211, 'Boston':1.395 ,'Boulder':1.101 , 'Charlotte':0.965, 'Charlottesville':1.044, 'Chicago':1.167, 'Cincinnati':0.868,
	'Corvallis':1.038, 'Dallas':1.017, 'Detroit':0.979, 'Fort Collins':1.194,'Hartford':1.254,'Houston':0.846,'Ithaca':0.956,'Las Vegas':0.981, 'Los Angeles':1.426,'Madison':1.001,'Miami':1.147,
	'Minneapolis':1.127, 'New Haven':1.268, 'New York City':1.830,'Orlando':1.030, 'Philadelphia':1.251,'Phoenix':1.204,'Pittsburgh':0.968,'Portland':1.108,'Raleigh':0.930,'Riverside':1.132,'Sacramento':1.205,
	'San Antonio':0.922,'San Diego':1.386,'San Francisco':1.625,'San Jose':1.514,'Seattle':1.188,'St. Louis':0.968, 'Tampa':0.925, 'Washington, D.C.':1.596}

    #[{city_name:{sweEntry: x, sweExp: x, sweSenior: x,...}}, ]
    salary_object = web_scrape.get_city_salary_nums()

    # c = {'Ann Arbor': {'sweEntry': x,}}
    for c in salary_object:
        # i = 'Ann Arbor'
        for i in c:
            #get city object
            cityName = City.objects.update_or_create(city_name = i, col_index = city_actual[i])[0]
            cityName.save()
            #get salary values
            try:
                sweEntry = c[i]["sweEntry"]
                print()
            except:
                sweEntry = 0

            try:
                sweMiddle = c[i]["sweExp"]
            except:
                sweMiddle = 0

            try:
                sweSenior = c[i]["sweSenior"]
            except:
                sweSenior = 0

            try:
                webEntry = c[i]["webdevEntry"]
            except:
                webEntry = 0

            try:
                webMiddle = c[i]["webdevExp"]
            except:
                webMiddle = 0

            try:
                webSenior = c[i]["webdevSenior"]
            except:
                webSenior = 0

            try:
                dbaEntry = c[i]["dbaEntry"]
            except:
                dbaEntry = 0

            try:
                dbaMiddle = c[i]["dbaExp"]
            except:
                dbaMiddle = 0

            try:
                dbaSenior = c[i]["dbaSenior"]
            except:
                dbaSenior = 0

            Salary.objects.update_or_create(city=cityName, sweEnt = sweEntry, sweMid=sweMiddle, sweSen=sweSenior, webEnt = webEntry,
            webMid = webMiddle, webSen=webSenior, dbaEnt=dbaEntry, dbaMid=dbaMiddle, dbaSen = dbaSenior)[0]

if __name__ == '__main__':
	print("Populating script!")
	populate()
	print('Population complete!')
