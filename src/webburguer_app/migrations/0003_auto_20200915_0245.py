# Generated by Django 3.0 on 2020-09-15 02:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webburguer_app', '0002_auto_20200912_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='burgueruser',
            name='franqueada',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webburguer_app.Franqueada'),
        ),
    ]
