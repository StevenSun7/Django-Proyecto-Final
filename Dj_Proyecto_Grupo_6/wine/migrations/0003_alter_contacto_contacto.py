# Generated by Django 3.2.18 on 2023-05-30 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wine', '0002_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacto',
            name='contacto',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]