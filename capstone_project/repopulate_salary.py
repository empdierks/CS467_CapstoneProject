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

    #[{city_name:{sweEntry: x, sweExp: x, sweSenior: x,...}}, ]
    salary_object = web_scrape.get_city_salary_nums()

    # c = {'Ann Arbor': {'sweEntry': x,}}
    for c in salary_object:
        # i = 'Ann Arbor'
        for i in c:
            #get city object
            cityName = City.objects.get(city_name = i)

            #get salary values
            try:
                sweEntry = c[i]["sweEntry"]
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

            Salary.objects.update_or_create(city=cityName, defaults= {'sweEnt': sweEntry, 'sweMid':sweMiddle, 'sweSen':sweSenior, 'webEnt': webEntry,
            'webMid': webMiddle, 'webSen':webSenior, 'dbaEnt':dbaEntry, 'dbaMid':dbaMiddle, 'dbaSen': dbaSenior})[0]

if __name__ == '__main__':
	print("Populating script!")
	populate()
	print('Population complete!')
