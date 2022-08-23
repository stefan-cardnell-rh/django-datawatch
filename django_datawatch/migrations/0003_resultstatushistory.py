# Generated by Django 3.2.7 on 2021-09-14 10:04

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('django_datawatch', '0002_auto_20180807_1508'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResultStatusHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('from_status', models.IntegerField(choices=[(0, 'Unknown'), (1, 'OK'), (2, 'Warning'), (3, 'Critical')], null=True, verbose_name='From status')),
                ('to_status', models.IntegerField(choices=[(0, 'Unknown'), (1, 'OK'), (2, 'Warning'), (3, 'Critical')], verbose_name='To status')),
                ('result', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='status_history', related_query_name='status_history', to='django_datawatch.result', verbose_name='Result')),
            ],
            options={
                'verbose_name': 'Result status history',
                'verbose_name_plural': 'Result status history',
            },
        ),
    ]