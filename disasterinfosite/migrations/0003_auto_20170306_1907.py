# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import disasterinfosite.models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0002_auto_20161003_2337'),
    ]

    operations = [
        migrations.CreateModel(
            name='LSLD_existing_features',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', default=disasterinfosite.models.LSLD_existing_features.getGroup)),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_steepslope',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=254)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', default=disasterinfosite.models.LSLD_steepslope.getGroup)),
            ],
        ),
        migrations.CreateModel(
            name='Summer_kingco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', default=disasterinfosite.models.Summer_kingco.getGroup)),
            ],
        ),
        migrations.CreateModel(
            name='Winter_kingco',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', default=disasterinfosite.models.Winter_kingco.getGroup)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_existing_features_filter',
            field=models.ForeignKey(to='disasterinfosite.LSLD_existing_features', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_steepslope_filter',
            field=models.ForeignKey(to='disasterinfosite.LSLD_steepslope', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Summer_kingco_filter',
            field=models.ForeignKey(to='disasterinfosite.Summer_kingco', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Winter_kingco_filter',
            field=models.ForeignKey(to='disasterinfosite.Winter_kingco', blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+'),
        ),
    ]
