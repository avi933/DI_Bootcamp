# Generated by Django 4.1 on 2022-09-06 12:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('legs', models.IntegerField()),
                ('weight', models.FloatField()),
                ('height', models.IntegerField()),
                ('speed', models.FloatField()),
                ('family', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.family')),
            ],
        ),
    ]
