# Generated by Django 3.2.4 on 2021-06-24 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='Prix_Vente',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='forme',
            field=models.CharField(choices=[('comprime', 'comprime'), ('sirop', 'sirop'), ('suppo', 'suppo')], max_length=15, null=True),
        ),
    ]
