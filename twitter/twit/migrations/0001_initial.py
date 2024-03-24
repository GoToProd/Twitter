# Generated by Django 5.0.3 on 2024-03-24 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(default='Anonymouse', max_length=32)),
                ('text', models.TextField(max_length=255)),
                ('created_timestamp', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'пост',
                'verbose_name_plural': 'посты',
            },
        ),
    ]
