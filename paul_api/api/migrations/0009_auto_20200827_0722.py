# Generated by Django 3.1 on 2020-08-27 07:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_auto_20200827_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='csvfieldmap',
            name='table',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='csv_field_mapping', to='api.table'),
        ),
    ]
