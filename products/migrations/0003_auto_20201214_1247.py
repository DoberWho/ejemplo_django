# Generated by Django 3.1.4 on 2020-12-14 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('products', '0002_auto_20201211_1251'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name']},
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(to='tags.Tag'),
        ),
        migrations.AlterModelTable(
            name='product',
            table='product',
        ),
    ]
