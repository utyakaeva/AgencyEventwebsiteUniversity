# Generated by Django 2.2.1 on 2019-06-07 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbiv_mechts', '0007_auto_20190606_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='generalschedule',
            name='duration',
        ),
        migrations.AddField(
            model_name='additionalservice',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='chip',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='comment',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='generalschedule',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='orderschedule',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='payment',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='scenario',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='service',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='tariff',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='worker',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='workerprice',
            name='fladDelete',
            field=models.TextField(null=True),
        ),
    ]
