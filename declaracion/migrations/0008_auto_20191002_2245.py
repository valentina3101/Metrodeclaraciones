# Generated by Django 2.2 on 2019-10-02 22:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('declaracion', '0007_remove_template_contenido_extra'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='pie',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='declaracion',
            name='fecha',
            field=models.DateField(default=datetime.date(2019, 10, 2)),
        ),
    ]
