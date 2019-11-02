# Generated by Django 2.1.2 on 2019-02-08 09:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20190128_1020'),
    ]

    operations = [
        migrations.CreateModel(
            name='DateAndTime',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='posts',
            name='publish',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Home.DateAndTime'),
        ),
    ]
