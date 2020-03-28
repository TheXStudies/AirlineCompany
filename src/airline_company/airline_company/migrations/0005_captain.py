# Generated by Django 3.0.4 on 2020-03-28 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_company', '0004_auto_20200328_1501'),
    ]

    operations = [
        migrations.CreateModel(
            name='Captain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('experience', models.IntegerField(help_text='Must be >10 years')),
                ('name', models.CharField(max_length=32)),
                ('surname', models.CharField(max_length=32)),
                ('salary', models.DecimalField(decimal_places=2, max_digits=12)),
                ('age', models.IntegerField()),
            ],
        ),
    ]
