# Generated by Django 3.1.1 on 2020-09-07 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_userprofile_dashboard_filters'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tablecolumn',
            name='name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
