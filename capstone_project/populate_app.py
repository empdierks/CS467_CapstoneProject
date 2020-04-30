import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'capstone_project.settings')

import django
django.setup()

## FAKE POPULATION script
import random
from capstone_app.models import City, Languages
from faker import Faker

fakegen = Faker()
city = ['Portland', 'Tampa', 'Boston', 'Atlanta', 'Phoenix', 'San Diego','Ann Arbor', 'San Francisco',
 'San Jose', 'Seattle', 'Sacramento', 'San Antonio', 'Riverside', 'Raleigh', 'Pittsburgh',
 'Philadelphia', 'Orlando', 'New York City', 'Minneapolis', 'Miami', 'Madison', 'Los Angeles', 'Las Vegas', 'Ithaca',
 'Houston', 'Fort Collins', 'Durham', 'Detroit', 'Dallas', 'Corvallis', 'Cincinatti', 'Chicago', 'Charlottesville',
 'Charlotte', 'Boulder', 'Baltimore', 'Austin']

def add_city(num):
    c = City.objects.get_or_create(city_name = city[num])[0] #tuple returns objects
    c.save()
    return c

def random_int():
    fake_num = fakegen.random_int(0, 100)
    return fake_num

def populate(N=5):
    Faker.seed(0)

    for entry in range(N):
        #get city of entry
        c = add_city(entry)

        #create fake data for languages
        fake_c = random_int()
        fake_cplus = random_int()
        fake_csharp = random_int()
        fake_dart = random_int()
        fake_go = random_int()
        fake_haskell = random_int()
        fake_html = random_int()
        fake_java = random_int()
        fake_javascript = random_int()
        fake_kotlin = random_int()
        fake_matLab = random_int()
        fake_obj_c  = random_int()
        fake_perl  = random_int()
        fake_php = random_int()
        fake_python = random_int()
        fake_r  = random_int()
        fake_ruby = random_int()
        fake_rust  = random_int()
        fake_scala = random_int()
        fake_swift = random_int()
        fake_typeScript = random_int()
        fake_visual_basic = random_int()
        fake_asp_net = random_int()
        fake_angular = random_int()
        fake_bootstrap = random_int()
        fake_django = random_int()
        fake_ember = random_int()
        fake_flask = random_int()
        fake_laravel = random_int()
        fake_node_js = random_int()
        fake_rails = random_int()
        fake_react = random_int()
        fake_spring = random_int()
        fake_vue_js = random_int()
        fake_ms_sql = random_int()
        fake_mongoDB = random_int()
        fake_my_sql = random_int()
        fake_postGreSql = random_int()
        fake_redis = random_int()
        fake_sqlite = random_int()

        #Create language entries for the city
        lang = Languages.objects.get_or_create(city=c, c=fake_c, c_plus = fake_cplus, c_sharp = fake_csharp,
        dart = fake_dart, go=fake_go, haskell=fake_haskell, html_css= fake_html, java=fake_java, javaScript=fake_javascript,
        kotlin=fake_kotlin, matLab=fake_matLab, obj_c=fake_matLab, perl =fake_perl, php=fake_php ,python =fake_python, r=fake_r,
        ruby=fake_ruby, rust=fake_rust, scala=fake_scala, swift=fake_swift, typeScript=fake_typeScript, visual_basic=fake_visual_basic,
        asp_net = fake_asp_net, angular=fake_angular, bootstrap=fake_bootstrap, django=fake_django, ember=fake_ember, flask=fake_flask,
        laravel = fake_laravel, node_js=fake_node_js, rails=fake_rails, react=fake_react, spring=fake_spring, vue_js=fake_vue_js, ms_sql=fake_ms_sql,
        mongoDB=fake_mongoDB, my_sql=fake_my_sql, postGreSql=fake_postGreSql, redis=fake_redis, sqlite=fake_sqlite)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print('Population complete!')
