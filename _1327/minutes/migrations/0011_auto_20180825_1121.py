# Generated by Django 2.0.8 on 2018-08-25 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('minutes', '0010_auto_20180825_1114'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='minutesdocument',
            options={'base_manager_name': 'objects', 'permissions': (('view_minutesdocument', 'User/Group is allowed to view those minutes'),), 'verbose_name': 'Minutes', 'verbose_name_plural': 'Minutes'},
        ),
    ]
