# Generated by Django 3.2.3 on 2021-05-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(default='0000000', editable=False, max_length=7),
        ),
    ]