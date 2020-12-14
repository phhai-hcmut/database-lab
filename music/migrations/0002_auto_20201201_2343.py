# Generated by Django 3.1.3 on 2020-12-01 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='artist',
        ),
        migrations.AddField(
            model_name='album',
            name='owner',
            field=models.ManyToManyField(related_name='album', to='music.Artist'),
        ),
        migrations.AlterField(
            model_name='credit',
            name='artist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='artist', to='music.artist'),
        ),
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='track', to='music.album'),
        ),
        migrations.AlterField(
            model_name='track',
            name='artist_credits',
            field=models.ManyToManyField(related_name='credit', through='music.Credit', to='music.Artist'),
        ),
    ]