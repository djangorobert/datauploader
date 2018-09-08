# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Submission',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('filename', models.CharField(max_length=150)),
                ('description', models.CharField(help_text=b'write a description of file', max_length=300)),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('audience', models.CharField(max_length=8, choices=[(b'Public', b'Public'), (b'Private', b'Private')])),
                ('file', models.FileField(null=True, upload_to=b'uploads', blank=True)),
                ('you', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
