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

	city_search_array = ['&l=Portland%2C+OR', '&l=Tampa%2C+FL', '&l=Boston%2C+MA', '&l=Atlanta%2C+GA', '&l=Phoenix%2C+AZ', '&l=San+Diego%2C+CA','&l=Ann+Arbor%2C+MI', '&l=San+Francisco%2C+CA', '&l=San+Jose%2C+CA', '&l=Seattle%2C+WA', '&l=Sacramento%2C+CA', '&l=San+Antonio%2C+TX', '&l=Riverside%2C+CA', '&l=Raleigh%2C+NC', '&l=Pittsburgh%2C+PA','&l=Philadelphia%2C+PA', '&l=Orlando%2C+FL', '&l=New+York+City%2C+NY', '&l=Minneapolis%2C+MN', '&l=Miami%2C+FL', '&l=Madison%2C+WI', '&l=Los+Angeles%2C+CA', '&l=Las+Vegas%2C+NV', '&l=Ithaca%2C+NY','&l=Houston%2C+TX', '&l=Fort+Collins%2C+CO', '&l=Durham%2C+NC', '&l=Detroit%2C+MI', '&l=Dallas%2C+TX', '&l=Corvallis%2C+OR', '&l=Cincinatti%2C+OH', '&l=Chicago%2C+IL', '&l=Charlottesville%2C+VA','&l=Charlotte%2C+NC', '&l=Boulder%2C+CO', '&l=Baltimore%2C+MD', '&l=Austin%2C+TX']
	city_array_actual = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'San Diego','Ann Arbor', 'San Francisco', 'Jose', 'Seattle', 'Sacramento', 'San Antonio', 'Riverside', 'Raleigh', 'Pittsburgh','Philadelphia', 'Orlando', 'New York City', 'Minneapolis', 'Miami', 'Madison', 'Los Angeles', 'Las Vegas', 'Ithaca','Houston', 'Fort Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville','Charlotte', 'Boulder', 'Baltimore', 'Austin']
	# lang_search_array = ["?q=python+software", "?q=sql+software", "?q=java+software", "?q=c+++software"]
	l_search_array = ["?q=c+software", "?q=c+++software", "?q=c%23+software", "?q=dart+software", "?q=go+software", "?q=haskell+software", "?q=html+css+software", "?q=java+software", "?q=javascript+software","?q=kotlin+software","?q=matlab+software","?q=objective+c+software","?q=perl+software","?q=python+software","?q=r+software","?q=ruby+software","?q=python+software","?q=scala+software","?q=swift+software","?q=typescript+software","?q=visual+basic+software","?q=asp.net+software","?q=angular+software","?q=bootstrap+software","?q=django+software","?q=ember+software","?q=flask+software","?q=laravel+software","?q=node+software","?q=redis+software","?q=react+software","?q=spring+software","?q=vue+software","?q=mssql+software","?q=mongo+software","?q=mysql+software","?q=postgressql+software","?q=redis+software","?q=sqlite+software"]
	
	pairs = [('C', 'c'), ('C++','c_plus'), ('C#', 'c_sharp'), ('Dart', 'dart'),('Go', 'go'), ('Haskell', 'haskell'),
    ('HTML-CSS','html_css'), ('Java', 'java'), ('JavaScript','javaScript'),('Kotlin', 'kotlin'),('MatLab','matLab'),
    ('Objective-C', 'obj_c'), ('Perl', 'perl'), ('PHP', 'php'),('Python','python'),('R', 'r'), ('Ruby', 'ruby'),
    ('Rust', 'rust'), ('Scala', 'scala'), ('Swift','swift'),('TypeScript','typeScript'),('Visual Basic','visual_basic'),
    ('ASP.NET','asp_net'),('Angular','angular'),('BootStrap','bootstrap'),('Django','django'),('Ember','ember'),
    ('Flask','flask'),('Laravel','laravel'),('Node.js','node_js'),('Rails','rails'),('React', 'react'),('Spring','spring'),
    ('Vue.js','vue_js'),('MS SQL Server','ms_sql'),('MongoDB','mongoDB'),('MySQL','my_sql'),('PostGreSQL','postGreSql'),
    ('Redis','redis'),('SQLite','sqlite')]

	# city_array_actual = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix']
	# city_search_array = ['&l=Portland%2C+OR', '&l=Tampa%2C+FL', '&l=Boston%2C+MA', '&l=Atlanta%2C+GA', '&l=Phoenix%2C+AZ']
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