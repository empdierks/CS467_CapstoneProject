import indeed_web_scraper as indeed
import monster_web_scraper as monster
import github_jobs_api_scraper as github

def combine_results():

	indeed_jobs = indeed.get_language_city_count()
	github_jobs = github.get_language_city_count()
	monster_jobs = monster.get_city_language_nums()

	combined_object = []
	pairs = [('C', 'C'), ('C++','C__2B__2B'), ('C#', 'c__23'), ('Dart', 'flutter'),('Go', 'go'), ('Haskell', 'haskell'),
	('HTML-CSS','HTML'), ('Java', 'java'), ('JavaScript','Javascript'),('Kotlin', 'Kotlin'),('MatLab','MatLab'),
	('Objective-C', 'objective-c'), ('Perl', 'Perl'), ('PHP', 'PHP'),('Python','Python'),('R', 'R'), ('Ruby', 'Ruby'),
	('Rust', 'Rust'), ('Scala', 'Scala'), ('Swift','Swift'),('TypeScript','TypeScript'),('Visual Basic','Visual-Basic'),
	('ASP.NET','ASP.NET'),('Angular','Angular'),('BootStrap','bootstrap'),('Django','django'),('Ember','ember'),
	('Flask','flask'),('Laravel','laravel'),('Node.js','node.js'),('Rails','Ruby-On-Rails'),('React', 'React'),('Spring','spring'),
	('Vue.js','Vue'),('MS SQL Server','ms-sql-server'),('MongoDB','mongoDB'),('MySQL','MySQL'),('PostGreSQL','postGreSQL'),
	('Redis','redis'),('SQLite','sqlite')]


	for i in range(len(indeed_jobs)):
		cityObject = {}
		indeed_dict = indeed_jobs[i]
		github_dict = github_jobs[i]
		monster_dict = monster_jobs[i]

		# print(indeed_dict)

		if indeed_dict['cityName'] == github_dict['cityName'] == monster_dict['cityName']:
			city = indeed_dict['cityName']
		else:
			city = 'invalidCity'

		
		if indeed_dict['langCounts'] and github_dict["langCounts"] and monster_dict['langCounts']:
			langCounts = {}
			for j in range(len(pairs)):
				language = pairs[j][0]

				try:
					indeed_language_result = indeed_dict['langCounts'][language]
				except KeyError:
					indeed_language_result = -10
				try:
					github_language_result = github_dict['langCounts'][language]
				except KeyError:
					github_language_result = -10
				try:
					monster_language_result = monster_dict['langCounts'][language]
				except KeyError:
					monster_language_result = -10

				monster_indeed_sum = indeed_language_result + monster_language_result
				monster_indeed_avg = monster_indeed_sum//2
				combined_language_result = monster_indeed_avg + github_language_result
				langCounts[language] = combined_language_result

		
		cityObject["cityName"] = city
		cityObject["langCounts"] = langCounts
		combined_object.append(cityObject)


	# print("Combined object: ")
	return combined_object


def main():
	# URL = "https://www.indeed.com/jobs?q=sql&l=New+York%2C+NY"
	# https://www.indeed.com/jobs?q=python+software&l=Hartford%2C+CT
	
	combined_object = combine_results()
	print(combined_object)

if __name__ == "__main__":
	main()

