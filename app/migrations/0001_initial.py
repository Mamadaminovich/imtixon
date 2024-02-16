# Generated by Django 5.0.2 on 2024-02-16 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_column='title', max_length=100)),
                ('author', models.CharField(db_column='author', max_length=100)),
                ('image', models.ImageField(upload_to='images/')),
                ('description', models.TextField(db_column='description', max_length=1000)),
                ('body', models.TextField(db_column='body', max_length=1000)),
            ],
        ),
    ]