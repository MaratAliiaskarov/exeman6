# Generated by Django 4.0.5 on 2022-07-02 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('guest_name', models.CharField(max_length=50, verbose_name='Name')),
                ('from_email', models.EmailField(max_length=50, verbose_name='from_email')),
                ('content', models.TextField(max_length=3000, verbose_name='Content')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Date')),
                ('status', models.CharField(choices=[('active', 'Active'), ('blocked', 'Blocked')], default='new', max_length=50, verbose_name='Status')),
            ],
            options={
                'verbose_name': 'Entry',
                'verbose_name_plural': 'Entryses',
                'db_table': 'note',
            },
        ),
    ]
