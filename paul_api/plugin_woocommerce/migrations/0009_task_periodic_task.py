# Generated by Django 3.1.3 on 2020-11-24 22:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0014_remove_clockedschedule_enabled'),
        ('plugin_woocommerce', '0008_auto_20201102_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='periodic_task',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='woocommerce_tasks', to='django_celery_beat.periodictask'),
        ),
    ]
