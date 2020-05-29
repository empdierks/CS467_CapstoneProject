import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone_project.settings')

import django
django.setup()

## POPULATION script
from capstone_app.models import City, Languages
import aggregate_results as combine

import urllib.request
import json
import requests


def populate():

	city_actual = {'Ann Arbor': 0.942 , 'Atlanta':1.025, 'Austin':0.925, 'Baltimore':1.211, 'Boston':1.395 ,'Boulder':1.101 , 'Charlotte':0.965, 'Charlottesville':1.044, 'Chicago':1.167, 'Cincinnati':0.868,
	'Corvallis':1.038, 'Dallas':1.017, 'Detroit':0.979, 'Fort Collins':1.194,'Hartford':1.254,'Houston':0.846,'Ithaca':0.956,'Las Vegas':0.981, 'Los Angeles':1.426,'Madison':1.001,'Miami':1.147,
	'Minneapolis':1.127, 'New Haven':1.268, 'New York City':1.830,'Orlando':1.030, 'Philadelphia':1.251,'Phoenix':1.204,'Pittsburgh':0.968,'Portland':1.108,'Raleigh':0.930,'Riverside':1.132,'Sacramento':1.205,
	'San Antonio':0.922,'San Diego':1.386,'San Francisco':1.625,'San Jose':1.514,'Seattle':1.188,'St. Louis':0.968, 'Tampa':0.925, 'Washington, D.C.':1.596}

	combined_object = combine.combine_results()

	for c in range(len(combined_object)):

		cityName = combined_object[c]["cityName"]
		city = City.objects.get_or_create(city_name = cityName, col_index = city_actual[cityName])[0]
		city.save()

		try:
			fake_c = combined_object[c]["langCounts"]["C"]
		except:
			fake_c = 0

		try:
			fake_cplus = combined_object[c]["langCounts"]["C++"]
		except:
			fake_cplus = 0

		try:
			fake_csharp = combined_object[c]["langCounts"]["C#"]
		except:
			fake_csharp = 0

		try:
			fake_dart = combined_object[c]["langCounts"]["Dart"]
		except:
			fake_dart = 0

		try:
			fake_go = combined_object[c]["langCounts"]["Go"]
		except:
			fake_go = 0

		try:
			fake_haskell = combined_object[c]["langCounts"]["Haskell"]
		except:
			fake_haskell = 0

		try:
			fake_html = combined_object[c]["langCounts"]["HTML-CSS"]
		except:
			fake_html = 0

		try:
			fake_java = combined_object[c]["langCounts"]["Java"]
		except:
			fake_java = 0

		try:
			fake_javascript = combined_object[c]["langCounts"]["JavaScript"]
		except:
			fake_javascript = 0

		try:
			fake_kotlin = combined_object[c]["langCounts"]["Kotlin"]
		except:
			fake_kotlin = 0

		try:
			fake_matLab = combined_object[c]["langCounts"]["MatLab"]
		except:
			fake_matLab = 0

		try:
			fake_obj_c  = combined_object[c]["langCounts"]["Objective-C"]
		except:
			fake_obj_c = 0

		try:
			fake_perl  = combined_object[c]["langCounts"]["Perl"]
		except:
			fake_perl = 0

		try:
			fake_php = combined_object[c]["langCounts"]["PHP"]
		except:
			fake_php = 0

		try:
			fake_python = combined_object[c]["langCounts"]["Python"]
		except:
			fake_python = 0

		try:
			fake_r  = combined_object[c]["langCounts"]["R"]
		except:
			fake_r = 0

		try:
			fake_ruby = combined_object[c]["langCounts"]["Ruby"]
		except:
			fake_ruby = 0

		try:
			fake_rust  = combined_object[c]["langCounts"]["Rust"]
		except:
			fake_rust = 0

		try:
			fake_scala = combined_object[c]["langCounts"]["Scala"]
		except:
			fake_scala = 0

		try:
			fake_swift = combined_object[c]["langCounts"]["Swift"]
		except:
			fake_swift = 0

		try:
			fake_typeScript = combined_object[c]["langCounts"]["TypeScript"]
		except:
			fake_typeScript = 0

		try:
			fake_visual_basic = combined_object[c]["langCounts"]["Visual Basic"]
		except:
			fake_visual_basic = 0

		try:
			fake_asp_net = combined_object[c]["langCounts"]["ASP.NET"]
		except:
			fake_asp_net = 0

		try:
			fake_angular = combined_object[c]["langCounts"]["Angular"]
		except:
			fake_angular = 0

		try:
			fake_bootstrap = combined_object[c]["langCounts"]["Bootstrap"]
		except:
			fake_bootstrap = 0

		try:
			fake_django = combined_object[c]["langCounts"]["Django"]
		except:
			fake_django = 0

		try:
			fake_ember = combined_object[c]["langCounts"]["Ember"]
		except:
			fake_ember = 0

		try:
			fake_flask = combined_object[c]["langCounts"]["Flask"]
		except:
			fake_flask = 0

		try:
			fake_laravel = combined_object[c]["langCounts"]["Laravel"]
		except:
			fake_laravel = 0

		try:
			fake_node_js = combined_object[c]["langCounts"]["Node.js"]
		except:
			fake_node_js = 0

		try:
			fake_rails = combined_object[c]["langCounts"]["Rails"]
		except:
			fake_rails = 0

		try:
			fake_react = combined_object[c]["langCounts"]["React"]
		except:
			fake_react = 0

		try:
			fake_spring = combined_object[c]["langCounts"]["Spring"]
		except:
			fake_spring = 0

		try:
			fake_vue_js = combined_object[c]["langCounts"]["Vue.js"]
		except:
			fake_vue_js = 0

		try:
			fake_ms_sql = combined_object[c]["langCounts"]["MS SQL Server"]
		except:
			fake_ms_sql = 0

		try:
			fake_mongoDB = combined_object[c]["langCounts"]["MongoDB"]
		except:
			fake_mongoDB = 0

		try:
			fake_my_sql = combined_object[c]["langCounts"]["MySQL"]
		except:
			fake_my_sql = 0

		try:
			fake_postGreSql = combined_object[c]["langCounts"]["PostGreSQL"]
		except:
			fake_postGreSql = 0

		try:
			fake_redis = combined_object[c]["langCounts"]["Redis"]
		except:
			fake_redis = 0

		try:
			fake_sqlite = combined_object[c]["langCounts"]["SQLite"]
		except:
			fake_sqlite = 0


		#############################################################################
		# # Testing subset of data
		#############################################################################

		# lang = Languages.objects.update_or_create(city=city, c=fake_c, c_plus = fake_cplus, c_sharp = fake_csharp,
        # dart = fake_dart, go=fake_go, haskell=fake_haskell, html_css= fake_html, java=fake_java, javaScript=fake_javascript)[0]

		lang = Languages.objects.update_or_create(city=city, c=fake_c, c_plus = fake_cplus, c_sharp = fake_csharp,
        dart = fake_dart, go=fake_go, haskell=fake_haskell, html_css= fake_html, java=fake_java, javaScript=fake_javascript,
        kotlin=fake_kotlin, matLab=fake_matLab, obj_c=fake_obj_c, perl=fake_perl, php=fake_php, python =fake_python, r=fake_r,
        ruby=fake_ruby, rust=fake_rust, scala=fake_scala, swift=fake_swift, typeScript=fake_typeScript, visual_basic=fake_visual_basic,
        asp_net = fake_asp_net, angular=fake_angular, bootstrap=fake_bootstrap, django=fake_django, ember=fake_ember, flask=fake_flask,
        laravel = fake_laravel, node_js=fake_node_js, rails=fake_rails, react=fake_react, spring=fake_spring, vue_js=fake_vue_js, ms_sql=fake_ms_sql,
        mongoDB=fake_mongoDB, my_sql=fake_my_sql, postGreSql=fake_postGreSql, redis=fake_redis, sqlite=fake_sqlite)[0]

if __name__ == '__main__':
	print("Populating script!")
	populate()
	print('Population complete!')
