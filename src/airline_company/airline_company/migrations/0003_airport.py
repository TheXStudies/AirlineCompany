# Generated by Django 3.0.4 on 2020-03-28 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('airline_company', '0002_airplane'),
    ]

    operations = [
        migrations.CreateModel(
            name='Airport',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('strip_size', models.IntegerField(help_text="Strip's size", max_length=5)),
                ('opening_date', models.DateField()),
                ('altitude', models.IntegerField(help_text="Airport's altitude", max_length=5)),
            ],
        ),
    ]
