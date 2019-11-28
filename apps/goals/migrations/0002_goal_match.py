# Generated by Django 2.2.7 on 2019-11-28 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('goals', '0001_initial'),
        ('matches', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='goal',
            name='match',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goals', to='matches.Match', verbose_name='match'),
        ),
    ]