import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone_project.settings')

import django
django.setup()

## POPULATION script
from capstone_app.models import City, Languages, Salary
from faker import Faker
import random



def populate():

	city_actual = {'Ann Arbor': 0.942 , 'Atlanta':1.025, 'Austin':0.925, 'Baltimore':1.211, 'Boston':1.395 ,'Boulder':1.101 , 'Charlotte':0.965, 'Charlottesville':1.044, 'Chicago':1.167, 'Cincinnati':0.868,
	'Corvallis':1.038, 'Dallas':1.017, 'Detroit':0.979, 'Fort Collins':1.194,'Hartford':1.254,'Houston':0.846,'Ithaca':0.956,'Las Vegas':0.981, 'Los Angeles':1.426,'Madison':1.001,'Miami':1.147,
	'Minneapolis':1.127, 'New Haven':1.268, 'New York City':1.830,'Orlando':1.030, 'Philadelphia':1.251,'Phoenix':1.204,'Pittsburgh':0.968,'Portland':1.108,'Raleigh':0.930,'Riverside':1.132,'Sacramento':1.205,
	'San Antonio':0.922,'San Diego':1.386,'San Francisco':1.625,'San Jose':1.514,'Seattle':1.188,'St. Louis':0.968, 'Tampa':0.925, 'Washington, D.C.':1.596}

	fake = Faker()

	for c in city_actual:
		#create City Table
		cityName = City.objects.update_or_create(city_name = c, defaults={'col_index': city_actual[c]})[0]

		#create fake Salary table
		#fake_sweE = fake.random_int(60000, 70000)
		#fake_sweM = fake.random_int(70000, 80000)
		#fake_sweS = fake.random_int(80000, 100000)
		#fake_wdE = fake.random_int(60000, 70000)
		#fake_wdM = fake.random_int(70000, 80000)
		#fake_wdS = fake.random_int(80000, 100000)
		#fake_dbaE = fake.random_int(60000, 70000)
		#fake_dbaM = fake.random_int(70000, 80000)
		#fake_dbaS = fake.random_int(80000, 100000)

		#salaries = Salary.objects.update_or_create(city=cityName, sweEnt=fake_sweE, sweMid =fake_sweM, sweSen = fake_sweS, webEnt=fake_wdE, webMid=fake_wdM, webSen=fake_wdS,
		#dbaEnt=fake_dbaE, dbaMid=fake_dbaM, dbaSen=fake_dbaS)[0]


		#create fake Languages table
		fake_c = fake.random_int(0, 200)
		fake_cplus = fake.random_int(0, 200)
		fake_csharp = fake.random_int(0, 200)
		fake_dart = fake.random_int(0, 200)
		fake_go = fake.random_int(0, 200)
		fake_haskell = fake.random_int(0, 200)
		fake_html = fake.random_int(0, 200)
		fake_java = fake.random_int(0, 200)
		fake_javascript = fake.random_int(0, 200)
		fake_kotlin = fake.random_int(0, 200)
		fake_matLab = fake.random_int(0, 200)
		fake_obj_c  = fake.random_int(0, 200)
		fake_perl  = fake.random_int(0, 200)
		fake_php = fake.random_int(0, 200)
		fake_python = fake.random_int(0, 200)
		fake_r  = fake.random_int(0, 200)
		fake_ruby = fake.random_int(0, 200)
		fake_rust  = fake.random_int(0, 200)
		fake_scala = fake.random_int(0, 200)
		fake_swift = fake.random_int(0, 200)
		fake_typeScript = fake.random_int(0, 200)
		fake_visual_basic = fake.random_int(0, 200)
		fake_asp_net = fake.random_int(0, 200)
		fake_angular = fake.random_int(0, 200)
		fake_bootstrap = fake.random_int(0, 200)
		fake_django = fake.random_int(0, 200)
		fake_ember = fake.random_int(0, 200)
		fake_flask = fake.random_int(0, 200)
		fake_laravel = fake.random_int(0, 200)
		fake_node_js = fake.random_int(0, 200)
		fake_rails = fake.random_int(0, 200)
		fake_react = fake.random_int(0, 200)
		fake_spring = fake.random_int(0, 200)
		fake_vue_js = fake.random_int(0, 200)
		fake_ms_sql = fake.random_int(0, 200)
		fake_mongoDB = fake.random_int(0, 200)
		fake_my_sql = fake.random_int(0, 200)
		fake_postGreSql = fake.random_int(0, 200)
		fake_redis = fake.random_int(0, 200)
		fake_sqlite = fake.random_int(0, 200)

		Languages.objects.update_or_create(city=cityName, defaults = {'c':fake_c, 'c_plus': fake_cplus, 'c_sharp': fake_csharp,
        'dart': fake_dart, 'go': fake_go, 'haskell': fake_haskell, 'html_css': fake_html, 'java':fake_java, 'javaScript':fake_javascript,
        'kotlin':fake_kotlin, 'matLab':fake_matLab, 'obj_c':fake_matLab, 'perl': fake_perl, 'php':fake_php , 'python': fake_python, 'r':fake_r,
        'ruby':fake_ruby, 'rust':fake_rust, 'scala':fake_scala, 'swift':fake_swift, 'typeScript':fake_typeScript, 'visual_basic': fake_visual_basic,
        'asp_net': fake_asp_net, 'angular':fake_angular, 'bootstrap':fake_bootstrap, 'django':fake_django, 'ember':fake_ember, 'flask': fake_flask,
        'laravel': fake_laravel, 'node_js':fake_node_js, 'rails':fake_rails, 'react':fake_react, 'spring':fake_spring, 'vue_js':fake_vue_js, 'ms_sql':fake_ms_sql,
        'mongoDB':fake_mongoDB, 'my_sql':fake_my_sql, 'postGreSql':fake_postGreSql, 'redis':fake_redis, 'sqlite':fake_sqlite})[0]


if __name__ == '__main__':
	print("populating script!")
	populate()
	print('Population complete!')
