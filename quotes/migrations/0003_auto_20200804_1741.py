# Generated by Django 3.1 on 2020-08-04 22:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quotes', '0002_auto_20200729_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quoterequest',
            name='contact',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quotes.contact'),
        ),
    ]
