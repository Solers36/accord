# Generated by Django 3.1.7 on 2022-04-08 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist_name', models.CharField(max_length=50, verbose_name='Исполнитель')),
            ],
            options={
                'verbose_name': 'Артист',
                'verbose_name_plural': 'Артисты',
            },
        ),
        migrations.CreateModel(
            name='Accord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song_title', models.CharField(max_length=150, verbose_name='Название произведения')),
                ('song_text', models.TextField(verbose_name='Аккорды и текст')),
                ('сhords_used', models.CharField(max_length=250, verbose_name='Используемые аккорды')),
                ('link_to_the_video', models.CharField(max_length=250, verbose_name='Ссылка на видео')),
                ('artist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.artist')),
            ],
            options={
                'verbose_name': 'Подбор аккордов',
                'verbose_name_plural': 'Подборы аккордов',
            },
        ),
    ]
