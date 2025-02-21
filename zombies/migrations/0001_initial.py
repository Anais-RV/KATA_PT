# Generated by Django 5.1.4 on 2024-12-18 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Superviviente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('heridas', models.IntegerField(default=0)),
                ('acciones', models.IntegerField(default=3)),
                ('experiencia', models.IntegerField(default=0)),
                ('nivel', models.CharField(choices=[('Azul', 'Azul'), ('Amarillo', 'Amarillo'), ('Naranja', 'Naranja'), ('Rojo', 'Rojo')], default='Azul', max_length=50)),
            ],
        ),
    ]
