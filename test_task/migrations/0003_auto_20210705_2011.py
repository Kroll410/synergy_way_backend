# Generated by Django 3.2.5 on 2021-07-05 20:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('test_task', '0002_auto_20210705_2001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 20, 11, 18, 851223, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 20, 11, 18, 851240, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_added',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 20, 11, 18, 851629, tzinfo=utc), editable=False),
        ),
        migrations.AlterField(
            model_name='user',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime(2021, 7, 5, 20, 11, 18, 851643, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='test_task.group'),
        ),
    ]
