# Generated by Django 4.0.2 on 2022-02-15 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trgovina', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='proizvodi',
            name='id',
            field=models.IntegerField(db_column='id', primary_key=True, serialize=False),
        ),
    ]