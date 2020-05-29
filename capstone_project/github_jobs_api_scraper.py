import urllib.request
import json
import random
import requests



def getGitHubResponse(url):
	operUrl = urllib.request.urlopen(url)
	if(operUrl.getcode()==200):
		data = operUrl.read()
		jsonData = json.loads(data)
	else:
		print("Error receiving data", operUrl.getcode())
	return jsonData

def get_language_count(city_search, lang_search):
	url = "https://jobs.github.com/positions.json?location="
	city_language_url = url + city_search + lang_search
	try:
		tech_response = getGitHubResponse(city_language_url)
		lang_count = len(tech_response)
	except:
		return 0
	return lang_count


def get_language_city_count():

	pairs = [('C', 'c'), ('C++','c_plus'), ('C#', 'c_sharp'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
    ('HTML-CSS','html_css'), ('Java', 'java'), ('JavaScript','javaScript'),('Kotlin', 'kotlin'),('MatLab','matLab'),
    ('Objective-C', 'obj_c'), ('Perl', 'perl'), ('PHP', 'php'),('Python','python'),('R', 'r'), ('Ruby', 'ruby'),
    ('Rust', 'rust'), ('Scala', 'scala'), ('Swift','swift'),('TypeScript','typeScript'),('Visual Basic','visual_basic'),
    ('ASP.NET','asp_net'),('Angular','angular'),('Bootstrap','bootstrap'),('Django','django'),('Ember','ember'),
    ('Flask','flask'),('Laravel','laravel'),('Node.js','node_js'),('Rails','rails'),('React', 'react'),('Spring','spring'),
    ('Vue.js','vue_js'),('MS SQL Server','ms_sql'),('MongoDB','mongoDB'),('MySQL','my_sql'),('PostGreSQL','postGreSql'),
    ('Redis','redis'),('SQLite','sqlite')]



	city_array_search = ['Ann+Arbor', 'Atlanta', 'Austin', 'Baltimore', 'Boston', 'Boulder', 'Charlotte', 'Charlottesville', 'Chicago', 'Cincinnati',
	'Corvallis', 'Dallas', 'Detroit','Fort+Collins', 'Hartford', 'Houston', 'Ithaca', 'Las+Vegas', 'Los+Angeles', 'Madison', 'Miami', 'Minneapolis',
	'New+Haven','New+York+City', 'Orlando', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland', 'Raleigh', 'Riverside', 'Sacramento', 'San+Antonio',
	'San+Diego', 'San+Francisco', 'San+Jose', 'Seattle', 'Saint+Louis', 'Tampa', 'Washington+DC']

	city_array_actual = ['Ann Arbor', 'Atlanta', 'Austin', 'Baltimore', 'Boston', 'Boulder', 'Charlotte', 'Charlottesville', 'Chicago', 'Cincinnati',
	'Corvallis', 'Dallas', 'Detroit','Fort Collins', 'Hartford', 'Houston', 'Ithaca', 'Las Vegas', 'Los Angeles', 'Madison', 'Miami', 'Minneapolis',
	'New Haven','New York City', 'Orlando', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland', 'Raleigh', 'Riverside', 'Sacramento', 'San Antonio',
	'San Diego', 'San Francisco', 'San Jose', 'Seattle', 'St. Louis', 'Tampa', 'Washington, D.C.']


	l_search_array = ["&search=c", "&search=c++", "&search=c#", "&search=flutter", "&search=go", "&search=haskell", 
	"&search=html", "&search=java","&search=javascript", "&search=kotlin", "&search=matlab", 
	"&search=objective+c", "&search=perl", "&search=php", "&search=python", "&search=r", "&search=ruby",
	"&search=rust","&search=scala", "&search=swift", "&search=typescript", "&search=visual+basic", 
	"&search=asp.net", "&search=angular", "&search=bootstrap", "&search=django", "&search=ember", 
	"&search=flask", "&search=laravel", "&search=node", "&search=rails", "&search=react", "&search=spring", 
	"&search=vue", "&search=mssql", "&search=mongodb", "&search=mysql", "&search=postgresql", 
	"&search=redis", "&search=sqlite"]

	################################################
	# Testing subset of data
	################################################
	# city_array_search = ['Ann+Arbor', 'Atlanta', 'Austin']
	# l_search_array = ['c', 'c++', 'c#', 'flutter', 'go', 'haskell', 'HTML', 'java', 'Javascript']
	# pairs = [('C', 'c'), ('C++','C++'), ('C#', 'c#'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
	# ('HTML-CSS','HTML'), ('Java', 'java'), ('JavaScript','Javascript')]
	# city_array_actual = ['Ann Arbor', 'Atlanta', 'Austin']

	cities_count = []
	for i in range(len(city_array_search)):
		# python_url = "https://www.indeed.com/jobs" + "?q=python+software" + city_search_array[i]
		count = {}
		for j in range(len(l_search_array)):
			lang_count = get_language_count(city_array_search[i], l_search_array[j])
			# print(lang_count)
			key = pairs[j][0]
			count[key] = lang_count


		cities_count.append({"cityName": city_array_actual[i], "langCounts":count})
	
	return cities_count

def main():
	# URL = "https://www.indeed.com/jobs?q=sql&l=New+York%2C+NY"
	# https://www.indeed.com/jobs?q=python+software&l=Hartford%2C+CT
	

	cities_count = get_language_city_count()
	print(cities_count) 

if __name__ == "__main__":
	main()