# Generated by Django 5.1.4 on 2024-12-14 13:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_fotografia_publicada_alter_fotografia_categoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='fotografia',
            name='data_fotografia',
            field=models.DateTimeField(default=datetime.datetime(2024, 12, 14, 10, 52, 9, 995233)),
        ),
        migrations.AlterField(
            model_name='fotografia',
            name='categoria',
            field=models.CharField(choices=[('Nebulosa', 'NEBULOSA'), ('Estrela', 'ESTRELA'), ('GALÁXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100),
        ),
    ]