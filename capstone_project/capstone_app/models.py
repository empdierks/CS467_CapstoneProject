from django.db import models

# Create your models here.
class City(models.Model):
    city_name = models.CharField(max_length=100)
    col_index = models.DecimalField(max_digits = 4, decimal_places =3)

    def __str__(self):
        return self.city_name

class Languages(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    c = models.IntegerField(default=0)
    c_plus = models.IntegerField(default=0) # C++
    c_sharp = models.IntegerField(default=0) # C#
    dart = models.IntegerField(default=0)
    go = models.IntegerField(default=0)
    haskell = models.IntegerField(default=0)
    html_css = models.IntegerField(default=0)
    java = models.IntegerField(default=0)
    javaScript = models.IntegerField(default=0)
    kotlin = models.IntegerField(default=0)
    matLab = models.IntegerField(default=0)
    obj_c = models.IntegerField(default=0)
    perl = models.IntegerField(default=0)
    php = models.IntegerField(default=0)
    python = models.IntegerField(default=0)
    r = models.IntegerField(default=0)
    ruby = models.IntegerField(default=0)
    rust = models.IntegerField(default=0)
    scala = models.IntegerField(default=0)
    swift = models.IntegerField(default=0)
    typeScript = models.IntegerField(default=0)
    visual_basic = models.IntegerField(default=0)
    asp_net = models.IntegerField(default=0)
    angular = models.IntegerField(default=0)
    bootstrap = models.IntegerField(default=0)
    django = models.IntegerField(default=0)
    ember = models.IntegerField(default=0)
    flask =models.IntegerField(default=0)
    laravel = models.IntegerField(default=0)
    node_js = models.IntegerField(default=0)
    rails = models.IntegerField(default=0)
    react = models.IntegerField(default=0)
    spring = models.IntegerField(default=0)
    vue_js = models.IntegerField(default=0)
    ms_sql = models.IntegerField(default=0) # ms sql server
    mongoDB = models.IntegerField(default=0)
    my_sql =models.IntegerField(default=0)
    postGreSql = models.IntegerField(default=0)
    redis = models.IntegerField(default=0)
    sqlite = models.IntegerField(default=0)

class Salary(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    sweEnt = models.IntegerField(default=0)
    sweMid = models.IntegerField(default=0)
    sweSen = models.IntegerField(default=0)
    webEnt = models.IntegerField(default=0)
    webMid = models.IntegerField(default=0)
    webSen = models.IntegerField(default=0)
    dbaEnt = models.IntegerField(default=0)
    dbaMid = models.IntegerField(default=0)
    dbaSen = models.IntegerField(default=0)
