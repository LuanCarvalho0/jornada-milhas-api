# Generated by Django 4.2.5 on 2023-10-17 21:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jornada_milhas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='')),
                ('nome', models.CharField(max_length=50)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=7)),
            ],
        ),
    ]
