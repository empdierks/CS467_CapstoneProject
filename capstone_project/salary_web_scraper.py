import requests
from bs4 import BeautifulSoup


def get_salaries(url):

    try:
        page = requests.get(url)
        soup = BeautifulSoup(page.content, 'html.parser')
        median = False

        salary_table = soup.find('table', {"class":"table-chart"})
        for row in salary_table.findAll('td'):
            if median == True:
                salary = row.text
                end = len(salary)
                sal_value = salary[1:end].replace(',', '')
                result = int(sal_value)
                return result
            if "50th" in row.text:
                median = True
    except:
        return 0

def get_city_salary_nums():

    query_locations = [('Ann Arbor','ann-arbor-mi'),('Atlanta','atlanta-ga'), ('Austin','austin-tx'), ('Baltimore','baltimore-md'),('Boston','boston-ma'), ('Boulder','boulder-co'),
    ('Charlotte','charlotte-nc'), ('Charlottesville','charlottesville-va'), ('Chicago','chicago-il'), ('Cincinnati','cincinnati-oh'),('Corvallis','corvallis-or'), ('Dallas','dallas-tx'),
    ('Detroit','detroit-mi'),('Fort Collins','fort-collins-co'), ('Hartford','hartford-ct'), ('Houston','houston-tx'), ('Ithaca','ithaca-ny'), ('Las Vegas','las-vegas-nv'),
    ('Los Angeles','los-angeles-ca'), ('Madison','madison-wi'), ('Miami','miami-fl'), ('Minneapolis','minneapolis-mn'),('New Haven','new-haven-ct'),('New York City','new-york-city-ny'),
    ('Orlando', 'orlando-fl'), ('Philadelphia','philadelphia-pa'), ('Phoenix','phoenix-az'), ('Pittsburgh','pittsburgh-pa'), ('Portland','portland-or'), ('Raleigh','raleigh-nc'),
    ('Riverside','riverside-ca'), ('Sacramento','sacramento-ca'), ('San Antonio','san-antonio-tx'),('San Diego','san-diego-ca'), ('San Francisco','san-francisco-ca'), ('San Jose','san-jose-ca'),
    ('Seattle','seattle-wa'), ('St. Louis','saint-louis-mo'), ('Tampa','tampa-fl'), ('Washington, D.C.','washington-dc')]

    query_jobs = [('sweEntry', '/benchmark/software-engineer-i'), ('sweExp','/benchmark/software-engineer-iii'), ('sweSenior','/benchmark/software-engineer-v'),('webdevEntry',
    '/alternate/web-applications-developer-entry'),('webdevExp','/alternate/web-applications-developer-experienced'), ('webdevSenior','/alternate/web-applications-developer-senior'),
    ('dbaEntry', '/alternate/dba-entry'), ('dbaExp','/alternate/dba-experienced'), ('dbaSenior','/alternate/dba-senior') ]

    ################################################
	# Testing subset of data
	################################################
    #query_locations = [('Ann Arbor','ann-arbor-mi'),('Atlanta','atlanta-ga'), ('Austin','austin-tx')]
    #query_jobs = [('dbaExp','/alternate/dba-experienced')]

    #[{city_name:{sweEntry: x, sweExp: x, sweSenior: x,...}}, ]
    completed_list = []

    for city in query_locations:
        salary_dict = {}
        inner_dict = {}
        city_name = city[0]

        for job in query_jobs:
            #example: https://www.salary.com/research/salary/benchmark/software-engineer-i-salary/chicago-il
            url = 'https://www.salary.com/research/salary' + job[1] + '-salary/'+ city[1]
            num = get_salaries(url)
            inner_dict[job[0]] = num
        salary_dict[city_name] = inner_dict
        completed_list.append(salary_dict)
    return completed_list

def main():
    completed_list = get_city_salary_nums()
    print(completed_list)


if __name__ == '__main__':
    main()
