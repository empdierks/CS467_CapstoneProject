import requests
import bs4
from bs4 import BeautifulSoup
import time



def get_language_count(lang_search, city_search):
	url = "https://www.indeed.com/jobs" + lang_search + city_search + '&radius=0'
	page = requests.get(url)
	soup = BeautifulSoup(page.text, "html.parser")
	try:
		phrase_extract = soup.find(id="searchCountPages")
		val = phrase_extract.text.split('<div id="searchCountPages">')[0]

		start = val.find('Page 1 of ') + 10
		end = val.find(' jobs', start)
		value = val[start:end].replace(',', '')
		result = int(value)
		# print(result)
		return result
	except:
		return 0

def get_language_city_count():

	city_search_array = ['&l=Ann+Arbor%2C+MI', '&l=Atlanta%2C+GA', '&l=Austin%2C+TX', '&l=Baltimore%2C+MD', '&l=Boston%2C+MA', '&l=Boulder%2C+CO', '&l=Charlotte%2C+NC', '&l=Charlottesville%2C+VA', '&l=Chicago%2C+IL', '&l=Cincinnati%2C+OH',
	'&l=Corvallis%2C+OR', '&l=Dallas%2C+TX', '&l=Detroit%2C+MI', '&l=Fort+Collins%2C+CO', '&l=Hartford%2C+CT', '&l=Houston%2C+TX', '&l=Ithaca%2C+NY', '&l=Las+Vegas%2C+NV', '&l=Los+Angeles%2C+CA', '&l=Madison%2C+WI', '&l=Miami%2C+FL', '&l=Minneapolis%2C+MN',
	'&l=New+Haven%2C+CT', '&l=New+York+City%2C+NY', '&l=Orlando%2C+FL', '&l=Philadelphia%2C+PA', '&l=Phoenix%2C+AZ', '&l=Pittsburgh%2C+PA', '&l=Portland%2C+OR', '&l=Raleigh%2C+NC', '&l=Riverside%2C+CA', '&l=Sacramento%2C+CA', '&l=San+Antonio%2C+TX',
	'&l=San+Diego%2C+CA','&l=San+Francisco%2C+CA', '&l=San+Jose%2C+CA', '&l=Seattle%2C+WA', '&l=St.+Louis%2C+MO', '&l=Tampa%2C+FL', '&l=Washington%2C+DC']

	l_search_array = ["?q=c+software", "?q=c+++software", "?q=c%23+software", "?q=flutter+software", "?q=go+software", "?q=haskell+software", 
	"?q=html+css+software", "?q=java+software", "?q=javascript+software","?q=kotlin+software","?q=matlab+software",
	"?q=objective+c+software","?q=perl+software", "?q=php+software","?q=python+software","?q=r+software","?q=ruby+software", 
	"?q=rust+software", "?q=scala+software","?q=swift+software","?q=typescript+software","?q=visual+basic+software",
	"?q=asp.net+software","?q=angular+software","?q=bootstrap+software", "?q=django+software","?q=ember+software",
	"?q=flask+software","?q=laravel+software","?q=node+software","?q=rails+software","?q=react+software","?q=spring+software",
	"?q=vue+software","?q=mssql+software","?q=mongo+software","?q=mysql+software","?q=postgresql+software",
	"?q=redis+software","?q=sqlite+software"]
	
	city_array_actual = ['Ann Arbor', 'Atlanta', 'Austin', 'Baltimore', 'Boston', 'Boulder', 'Charlotte', 'Charlottesville', 'Chicago', 'Cincinnati',
	'Corvallis', 'Dallas', 'Detroit','Fort Collins', 'Hartford','Houston', 'Ithaca', 'Las Vegas', 'Los Angeles', 'Madison', 'Miami', 'Minneapolis',
	'New Haven','New York City', 'Orlando', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland', 'Raleigh', 'Riverside', 'Sacramento', 'San Antonio',
	'San Diego', 'San Francisco', 'San Jose', 'Seattle', 'Saint Louis', 'Tampa', 'Washington DC']
	
	pairs = [('C', 'c'), ('C++','c_plus'), ('C#', 'c_sharp'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
    ('HTML-CSS','html_css'), ('Java', 'java'), ('JavaScript','javaScript'),('Kotlin', 'kotlin'),('MatLab','matLab'),
    ('Objective-C', 'obj_c'), ('Perl', 'perl'), ('PHP', 'php'),('Python','python'),('R', 'r'), ('Ruby', 'ruby'),
    ('Rust', 'rust'), ('Scala', 'scala'), ('Swift','swift'),('TypeScript','typeScript'),('Visual Basic','visual_basic'),
    ('ASP.NET','asp_net'),('Angular','angular'),('BootStrap','bootstrap'),('Django','django'),('Ember','ember'),
    ('Flask','flask'),('Laravel','laravel'),('Node.js','node_js'),('Rails','rails'),('React', 'react'),('Spring','spring'),
    ('Vue.js','vue_js'),('MS SQL Server','ms_sql'),('MongoDB','mongoDB'),('MySQL','my_sql'),('PostGreSQL','postGreSql'),
    ('Redis','redis'),('SQLite','sqlite')]

	################################################
	# Testing subset of data
	################################################
	# city_search_array = ['&l=Ann+Arbor%2C+MI', '&l=Atlanta%2C+GA', '&l=Austin%2C+TX']
	# l_search_array = ['?q=c+software', '?q=c+++software', '?q=c%23+software', '?q=dart+software', '?q=go+software', '?q=haskell+software', '?q=html+css+software', '?q=java+software', '?q=javascript+software']
	# pairs = [('C', 'c'), ('C++','C++'), ('C#', 'c#'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
	# ('HTML-CSS','HTML'), ('Java', 'java'), ('JavaScript','Javascript')]
	# city_array_actual = ['Ann Arbor', 'Atlanta', 'Austin']

	cities_count = []
	for i in range(len(city_search_array)):
		# python_url = "https://www.indeed.com/jobs" + "?q=python+software" + city_search_array[i]
		count = {}
		for j in range(len(l_search_array)):
			lang_count = get_language_count(l_search_array[j], city_search_array[i])
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