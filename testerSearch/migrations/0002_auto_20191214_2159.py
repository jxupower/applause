# Generated by Django 3.0 on 2019-12-14 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('testerSearch', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bug',
            name='tester',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='testerSearch.Tester'),
        ),
        migrations.AlterField(
            model_name='device',
            name='tester',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='testerSearch.Tester'),
        ),
    ]
