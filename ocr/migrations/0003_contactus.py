# Generated by Django 3.2.4 on 2021-06-09 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ocr', '0002_alter_filemodel_rec_lang'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('phone', models.CharField(default='', max_length=10)),
                ('desc', models.TextField()),
            ],
        ),
    ]
