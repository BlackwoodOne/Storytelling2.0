# Generated by Django 2.0.5 on 2018-07-01 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20180609_1357'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlayerName',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('used', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
            ],
        ),
        migrations.AlterField(
            model_name='player',
            name='playing',
            field=models.IntegerField(default=0),
        ),
    ]
