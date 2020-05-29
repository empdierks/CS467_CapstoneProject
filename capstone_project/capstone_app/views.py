from django.shortcuts import render
from django.http import JsonResponse
from capstone_app.models import City, Languages, Salary
import json
from django.core import serializers

# Create your views here.
def index(request):
    return render(request, 'homepage/homepage.html')

def post_models(request):

    pairs = [('C', 'c'), ('C++','c_plus'), ('C#', 'c_sharp'), ('Dart', 'dart'),('Go', 'go'), ('Haskell', 'haskell'),
    ('HTML-CSS','html_css'), ('Java', 'java'), ('JavaScript','javaScript'),('Kotlin', 'kotlin'),('MatLab','matLab'),
    ('Objective-C', 'obj_c'), ('Perl', 'perl'), ('PHP', 'php'),('Python','python'),('R', 'r'), ('Ruby', 'ruby'),
    ('Rust', 'rust'), ('Scala', 'scala'), ('Swift','swift'),('TypeScript','typeScript'),('Visual Basic','visual_basic'),
    ('ASP.NET','asp_net'),('Angular','angular'),('Bootstrap','bootstrap'),('Django','django'),('Ember','ember'),
    ('Flask','flask'),('Laravel','laravel'),('Node.js','node_js'),('Rails','rails'),('React', 'react'),('Spring','spring'),
    ('Vue.js','vue_js'),('MS SQL Server','ms_sql'),('MongoDB','mongoDB'),('MySQL','my_sql'),('PostGreSQL','postGreSql'),
    ('Redis','redis'),('SQLite','sqlite')]

    job_roles = ['sweEnt', 'sweMid', 'sweSen', 'webEnt', 'webMid', 'webSen', 'dbaEnt', 'dbaMid', 'dbaSen']

    qs = list(Languages.objects.select_related('city').values(
        'city__city_name','city__col_index', 'c', 'c_plus', 'c_sharp', 'dart', 'go', 'haskell', 'html_css', 'java',
        'javaScript', 'kotlin', 'matLab', 'obj_c', 'perl', 'php', 'python', 'r', 'ruby', 'rust',
        'scala', 'swift', 'typeScript', 'visual_basic', 'asp_net', 'angular', 'bootstrap', 'django',
        'ember','flask','laravel', 'node_js', 'rails', 'react','spring','vue_js','ms_sql', 'mongoDB',
        'my_sql','postGreSql', 'redis', 'sqlite'))

    salary_qs = list(Salary.objects.select_related('city').values(
        'city__city_name', 'sweEnt', 'sweMid', 'sweSen', 'webEnt', 'webMid', 'webSen', 'dbaEnt', 'dbaMid', 'dbaSen'
    ))

    converted_list = [] #completed list of dictionary values [{cityName: value, COLidx: value, langCounts:{}, MedSalaries:{} }]
    pair_index = 0

    for d in qs:
        city_dict = {}
        inner_dict = {}
        salary_dict = {}

        for key in d:
            if key == 'city__city_name':
                city_dict['cityName'] = d[key]
            elif key == 'city__col_index':
                city_dict['COLidx'] = d[key]
            else:
                for p in pairs:
                    if key in p:
                        inner_dict[pairs[pair_index][0]] = d[key]
                        pair_index = pair_index+1
                        if pair_index == len(pairs):
                            pair_index = 0
        city_dict["langCounts"]= inner_dict

        for salary in salary_qs:
            if salary['city__city_name'] == d['city__city_name']:
                for role in job_roles:
                    salary_dict[role] = salary[role]
                city_dict["medSalaries"] = salary_dict
                break

        converted_list.append(city_dict)
    #qs_names = list(City.objects.values())
    #qs_langs = list(Languages.objects.values())
    #lang = list(Languages.objects.values()) # values() creates querySet like iterable dictionary
    return JsonResponse(converted_list, safe = False)
