# Generated by Django 3.1.3 on 2021-06-17 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Popup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('space', 'space'), ('cnt223', 'cnt223')], max_length=10)),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
