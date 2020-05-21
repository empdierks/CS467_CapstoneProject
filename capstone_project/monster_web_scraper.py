import requests
from bs4 import BeautifulSoup


def get_nums(url):

	headers = requests.utils.default_headers()
	headers.update({
			'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0',

	})

	page = requests.get(url, headers=headers)
	soup = BeautifulSoup(page.content, 'html.parser')

	#See if any matches in city
	#job_match = soup.find('h1', class_='pivot block')
	try:
		jobs_figure = soup.find('h2', class_='figure')
		values = jobs_figure.text.strip()

		#https://www.kite.com/python/answers/how-to-extract-integers-from-a-string-in-python
		# print(values)
		# print(type(values))
		# words = values.split()  #separates it into '(4', 'Jobs', 'Found)'
		# return int(words[0][1])  #prints just 4
		start = values.find('(') + 1
		end = values.find(' Jobs', start)
		value = values[start:end].replace(',', '')
		# print(value)
		result = int(value)
		return result
	except:
		return 0

	#if job_match.text.strip() == "Sorry, we didn't find any jobs matching your criteria":
		#return 0


	#elif job_match.text.strip() == "Sorry, we didn't find any jobs matching your criteria":
		#return 0
		#find all job links
		#results = soup.find(id='ResultsContainer')
		#job_elems = results.find_all('section', class_='card-content')

		#finds all job links
		#for job_elem in job_elems:
			#link = job_elem.a
			#if None == link:
				#continue
			#print(link.get('href'))


def get_city_language_nums():
<<<<<<< HEAD
	query_locations = ['Ann-Arbor-MI', 'Atlanta-GA', 'Austin-TX', 'Baltimore-MD', 'Boston-MA', 'Boulder-CO', 'Charlotte-NC', 'Charlottesville-VA', 'Chicago-IL', 'Cincinnati-OH',
=======
	query_locations = ['Ann-Arbor-MI', 'Atlanta-GA', 'Austin-TX', 'Baltimore-MD', 'Boston-MA', 'Boulder-CO', 'Charlotte-NC', 'Charlottesville-VA', 'Chicago-IL', 'Cincinatti-OH',
>>>>>>> d6139dd7ccf5cf742192eaa4ed5da4bc15af52bd
	'Corvallis-OR', 'Dallas-TX', 'Detroit-MI','Fort-Collins-CO', 'Hartford-CT', 'Houston-TX', 'Ithaca-NY', 'Las-Vegas-NV', 'Los-Angeles-CA', 'Madison-WI', 'Miami-FL', 'Minneapolis-MN',
	'New-Haven-CT','New-York-City-NY', 'Orlando-FL', 'Philadelphia-PA', 'Phoenix-AZ', 'Pittsburgh-PA', 'Portland-OR', 'Raleigh-NC', 'Riverside-CA', 'Sacramento-CA', 'San-Antonio-TX',
	'San-Diego-CA', 'San-Francisco-CA', 'San-Jose-CA', 'Seattle-WA', 'Saint-Louis-MO', 'Tampa-FL', 'Washington-DC']


	query_language = ['C', 'C__2B__2B', 'c__23', 'flutter', 'go', 'haskell', 'HTML', 'java', 'Javascript', 'Kotlin','Matlab', 'objective-c',
	'Perl', 'PHP', 'Python', 'R', 'Ruby', 'Rust', 'Scala', 'Swift', 'TypeScript', 'Visual-Basic', 'ASP.NET', 'Angular', 'bootstrap', 'django',
	'ember', 'flask', 'laravel', 'node.js', 'Ruby-On-Rails', 'React', 'spring', 'Vue', 'ms-sql-server', 'mongoDB','MySQL', 'postGreSQL', 'redis','sqlite']
	# C__2B__2B instead of C++
	# c_23 instead of c#
	#flutter instead of dart
	#HTML instead of HTML-CSS

	pairs = [('C', 'C'), ('C++','C__2B__2B'), ('C#', 'c__23'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
	('HTML-CSS','HTML'), ('Java', 'java'), ('JavaScript','Javascript'),('Kotlin', 'Kotlin'),('MatLab','MatLab'),
	('Objective-C', 'objective-c'), ('Perl', 'Perl'), ('PHP', 'PHP'),('Python','Python'),('R', 'R'), ('Ruby', 'Ruby'),
	('Rust', 'Rust'), ('Scala', 'Scala'), ('Swift','Swift'),('TypeScript','TypeScript'),('Visual Basic','Visual-Basic'),
	('ASP.NET','ASP.NET'),('Angular','Angular'),('BootStrap','bootstrap'),('Django','django'),('Ember','ember'),
	('Flask','flask'),('Laravel','laravel'),('Node.js','node.js'),('Rails','Ruby-On-Rails'),('React', 'React'),('Spring','spring'),
	('Vue.js','Vue'),('MS SQL Server','ms-sql-server'),('MongoDB','mongoDB'),('MySQL','MySQL'),('PostGreSQL','postGreSQL'),
	('Redis','redis'),('SQLite','sqlite')]

<<<<<<< HEAD
	locations = ['Ann Arbor', 'Atlanta', 'Austin', 'Baltimore', 'Boston', 'Boulder', 'Charlotte', 'Charlottesville', 'Chicago', 'Cincinnati',
=======
	locations = ['Ann Arbor', 'Atlanta', 'Austin', 'Baltimore', 'Boston', 'Boulder', 'Charlotte', 'Charlottesville', 'Chicago', 'Cincinatti',
>>>>>>> d6139dd7ccf5cf742192eaa4ed5da4bc15af52bd
	'Corvallis', 'Dallas', 'Detroit','Fort Collins', 'Hartford','Houston', 'Ithaca', 'Las Vegas', 'Los Angeles', 'Madison', 'Miami', 'Minneapolis',
	'New Haven','New York City', 'Orlando', 'Philadelphia', 'Phoenix', 'Pittsburgh', 'Portland', 'Raleigh', 'Riverside', 'Sacramento', 'San Antonio',
	'San Diego', 'San Francisco', 'San Jose', 'Seattle', 'Saint Louis', 'Tampa', 'Washington DC']

	################################################
	# Testing subset of data
	################################################
	# query_locations = ['Ann-Arbor-MI', 'Atlanta-GA', 'Austin-TX']
	# query_language = ['C', 'C__2B__2B', 'c__23', 'flutter', 'go', 'haskell', 'HTML', 'java', 'Javascript']
	# pairs = [('C', 'C'), ('C++','C__2B__2B'), ('C#', 'c__23'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
	# ('HTML-CSS','HTML'), ('Java', 'java'), ('JavaScript','Javascript')]
	# locations = ['Ann Arbor', 'Atlanta', 'Austin']

	completed_list = []
	loc_index = 0
	lang_index=0

	job_query = '-software'
	# radius = 5
	# date_posted = 30

	#URL = 'https://www.monster.com/jobs/search/?q=C-software&rad=5&where=Seattle-WA&tm=30'
	#print(get_nums(URL))

	#example: https://www.monster.com/jobs/search/?q=flutter-software&rad=5&where=Miami-FL&tm=30
	for city in query_locations:
		city_dict = {}
		inner_dict = {}

		city_dict['cityName'] = locations[loc_index]
		loc_index = loc_index+1
		if loc_index == len(locations):
			loc_index = 0

		for lang in query_language:
			# url = 'https://www.monster.com/jobs/search?q='+lang+job_query+'&rad='+str(radius)+'&where='+city+'&tm='+str(date_posted)
			# url = 'https://www.monster.com/jobs/search?q='+lang+job_query+'&rad='+str(radius)+'&where='+city+'&tm='
			url = 'https://www.monster.com/jobs/search?q='+lang+job_query+'&where='+city
			# print(url)
			# print('Location: '+locations[loc_index-1] + ' Lang: '+pairs[lang_index][0])

			num = get_nums(url)
			# print(num)

			inner_dict[pairs[lang_index][0]] = num
			lang_index = lang_index +1
			if lang_index == len(pairs):
				lang_index = 0
		city_dict['langCounts'] = inner_dict
		completed_list.append(city_dict)

	return completed_list


def main():

	completed_list = get_city_language_nums()
	print(completed_list)

#URL = 'https://www.monster.com/jobs/search/?q=sqlite-software&rad=5&where=Washington-DC&tm=30'
#print(get_nums(URL))


	#title_elem = job_elem.find('h2', class_='title')
	#company_elem = job_elem.find('div', class_='company')
	#location_elem = job_elem.find('div', class_='location')
	#if None in (title_elem):
		#continue
	#print(title_elem.text.strip())
	#print(company_elem.text.strip())
	#print(location_elem.text.strip())
	#print()
	#print(job_elem, end='\n'*2)
if __name__ == '__main__':
	main()
