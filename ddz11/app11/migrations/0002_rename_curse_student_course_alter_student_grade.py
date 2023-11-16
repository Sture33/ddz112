# Generated by Django 4.2.6 on 2023-11-14 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app11', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='curse',
            new_name='course',
        ),
        migrations.AlterField(
            model_name='student',
            name='grade',
            field=models.CharField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10'), ('11', '11'), ('12', '12')], default=1, max_length=255),
        ),
    ]