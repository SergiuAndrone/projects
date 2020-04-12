# Generated by Django 3.0.5 on 2020-04-12 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='gradinitaModel',
            fields=[
                ('nume', models.CharField(help_text='Numele gradinitei', max_length=30, primary_key=True, serialize=False)),
                ('adresa', models.CharField(help_text='Adresa', max_length=50)),
                ('telefon', models.CharField(help_text='Telefon', max_length=15)),
                ('email', models.EmailField(help_text='Email', max_length=15)),
                ('website', models.CharField(help_text='Website', max_length=30)),
                ('capacitate', models.IntegerField(help_text='Capacitate copii')),
                ('tip', models.CharField(default=None, help_text='Gradinita privata sau de stat', max_length=10)),
                ('sector', models.CharField(default=None, help_text='Sectorul gradinitei', max_length=15)),
            ],
            options={
                'ordering': ['-nume'],
            },
        ),
    ]
