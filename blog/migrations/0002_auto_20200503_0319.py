# Generated by Django 3.0.5 on 2020-05-03 03:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='published',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now, verbose_name='piblished at'),
            preserve_default=False,
        ),
    ]