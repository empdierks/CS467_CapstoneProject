# Generated by Django 3.0.3 on 2020-05-24 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('capstone_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='col_index',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sweEnt', models.IntegerField(default=0)),
                ('sweMid', models.IntegerField(default=0)),
                ('sweExp', models.IntegerField(default=0)),
                ('webEnt', models.IntegerField(default=0)),
                ('webMid', models.IntegerField(default=0)),
                ('webExp', models.IntegerField(default=0)),
                ('dbaEnt', models.IntegerField(default=0)),
                ('dbaMid', models.IntegerField(default=0)),
                ('dbaExp', models.IntegerField(default=0)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='capstone_app.City')),
            ],
        ),
    ]
