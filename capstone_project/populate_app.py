import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone_project.settings')

import django
django.setup()

## POPULATION script
from capstone_app.models import City, Languages
import urllib.request
import json
import requests

def getGitHubResponse(url):
	operUrl = urllib.request.urlopen(url)
	if(operUrl.getcode()==200):
		data = operUrl.read()
		jsonData = json.loads(data)
	else:
		print("Error receiving data", operUrl.getcode())
	return jsonData

def get_language_count(city_url, lang_search):
	city_language_url = city_url + lang_search
	try:
		tech_response = getGitHubResponse(city_language_url)
		lang_count = len(tech_response)
	except:
		return -1
	return lang_count


def populate():
	city_array_actual = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'San Diego','Ann Arbor', 'San Francisco', 'Jose', 'Seattle', 'Sacramento', 'San Antonio', 'Riverside', 'Raleigh', 'Pittsburgh','Philadelphia', 'Orlando', 'New York City', 'Minneapolis', 'Miami', 'Madison', 'Los Angeles', 'Las Vegas', 'Ithaca','Houston', 'Fort Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville','Charlotte', 'Boulder', 'Baltimore', 'Austin']
	city_array_search = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'Diego','Ann Arbor', 'Francisco', 'Jose', 'Seattle', 'Sacramento', 'Antonio', 'Riverside', 'Raleigh', 'Pittsburgh','Philadelphia', 'Orlando', 'NYC', 'Minneapolis', 'Miami', 'Madison', 'Angeles', 'Vegas', 'Ithaca','Houston', 'Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville','Charlotte', 'Boulder', 'Baltimore', 'Austin']

	for c in range(len(city_array_search)):
		city = City.objects.get_or_create(city_name = city_array_actual[c])[0]
		city.save()

		city_url = "https://jobs.github.com/positions.json?location=" + city_array_search[c]

		try:
			fake_c = get_language_count(city_url, "&search=c")
			#print(fake_c)
			fake_cplus = get_language_count(city_url, "&search=c++")
			fake_csharp = get_language_count(city_url, "&search=c#")
			fake_dart = get_language_count(city_url, "&search=dart")
			fake_go = get_language_count(city_url, "&search=go")
			fake_haskell = get_language_count(city_url, "&search=haskell")
			fake_html = get_language_count(city_url, "&search=html")
			fake_java = get_language_count(city_url, "&search=java")
			fake_javascript = get_language_count(city_url, "&search=javascript")
			fake_kotlin = get_language_count(city_url, "&search=kotlin")
			fake_matLab = get_language_count(city_url, "&search=matlab")
			fake_obj_c  = get_language_count(city_url, "&search=objective")
			fake_perl  = get_language_count(city_url, "&search=perl")
			fake_php = get_language_count(city_url, "&search=php")
			fake_python = get_language_count(city_url, "&search=python")
			fake_r  = get_language_count(city_url, "&search=r")
			fake_ruby = get_language_count(city_url, "&search=ruby")
			fake_rust  = get_language_count(city_url, "&search=rust")
			fake_scala = get_language_count(city_url, "&search=scala")
			fake_swift = get_language_count(city_url, "&search=swift")
			fake_typeScript = get_language_count(city_url, "&search=typescript")
			fake_visual_basic = get_language_count(city_url, "&search=visual")
			fake_asp_net = get_language_count(city_url, "&search=asp")
			fake_angular = get_language_count(city_url, "&search=angular")
			fake_bootstrap = get_language_count(city_url, "&search=bootscrap")
			fake_django = get_language_count(city_url, "&search=django")
			fake_ember = get_language_count(city_url, "&search=ember")
			fake_flask = get_language_count(city_url, "&search=flask")
			fake_laravel = get_language_count(city_url, "&search=laravel")
			fake_node_js = get_language_count(city_url, "&search=node")
			fake_rails = get_language_count(city_url, "&search=rails")
			fake_react = get_language_count(city_url, "&search=react")
			fake_spring = get_language_count(city_url, "&search=spring")
			fake_vue_js = get_language_count(city_url, "&search=vue")
			fake_ms_sql = get_language_count(city_url, "&search=mssql")
			fake_mongoDB = get_language_count(city_url, "&search=mongodb")
			fake_my_sql = get_language_count(city_url, "&search=mysql")
			fake_postGreSql = get_language_count(city_url, "&search=postgresql")
			fake_redis = get_language_count(city_url, "&search=redis")
			fake_sqlite = get_language_count(city_url, "&search=sqlite")
		except:
			pass

		lang = Languages.objects.get_or_create(city=city, c=fake_c, c_plus = fake_cplus, c_sharp = fake_csharp,
        dart = fake_dart, go=fake_go, haskell=fake_haskell, html_css= fake_html, java=fake_java, javaScript=fake_javascript,
        kotlin=fake_kotlin, matLab=fake_matLab, obj_c=fake_matLab, perl =fake_perl, php=fake_php ,python =fake_python, r=fake_r,
        ruby=fake_ruby, rust=fake_rust, scala=fake_scala, swift=fake_swift, typeScript=fake_typeScript, visual_basic=fake_visual_basic,
        asp_net = fake_asp_net, angular=fake_angular, bootstrap=fake_bootstrap, django=fake_django, ember=fake_ember, flask=fake_flask,
        laravel = fake_laravel, node_js=fake_node_js, rails=fake_rails, react=fake_react, spring=fake_spring, vue_js=fake_vue_js, ms_sql=fake_ms_sql,
        mongoDB=fake_mongoDB, my_sql=fake_my_sql, postGreSql=fake_postGreSql, redis=fake_redis, sqlite=fake_sqlite)[0]

if __name__ == '__main__':
	print("populating script!")
	populate()
	print('Population complete!')
