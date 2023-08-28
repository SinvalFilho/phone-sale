# Generated by Django 4.2.3 on 2023-07-30 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_celular_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='celular',
            name='data_atualizacao',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='celular',
            name='publicada',
            field=models.BooleanField(default=False),
        ),
    ]
