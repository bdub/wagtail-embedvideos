# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 02:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.models


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('wagtail_embed_videos', '0003_auto_20150817_1256'),
    ]

    operations = [
        migrations.AddField(
            model_name='embedvideo',
            name='collection',
            field=models.ForeignKey(default=wagtail.wagtailcore.models.get_root_collection_id, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailcore.Collection', verbose_name='collection'),
        ),
        migrations.AlterField(
            model_name='embedvideo',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='embedvideo',
            name='uploaded_by_user',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Uploader'),
        ),
    ]