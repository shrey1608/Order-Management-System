# Generated by Django 3.0.5 on 2020-04-18 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_auto_20200418_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='profilepic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]