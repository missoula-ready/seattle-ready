# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import disasterinfosite.models
import django.db.models.deletion
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQ_Liquefact_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_Liquefact_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Nisqual68_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_Nisqual68_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQ_SeattleFault72_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_SeattleFault72_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Tsunami_SeaFault72_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_Tsunami_SeaFault72_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='EQ_URM_DensityZones_seattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.EQ_URM_DensityZones_seattle.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Fire_WUI_kingco_only',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Fire_WUI_kingco_only.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood_100yr_wUrban_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_100yr_wUrban_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood_500yr_wUrban_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_500yr_wUrban_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood_CMZ_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_CMZ_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood_DamInundation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_DamInundation.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Flood_nearest_sand_distr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Flood_nearest_sand_distr.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Hubs_Nearest_seattle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Hubs_Nearest_seattle.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_ExistingAreas_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_ExistingAreas_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='LSLD_Prone_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.LSLD_Prone_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.CreateModel(
            name='Volcano_Lahar_kingco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
                ('group', models.ForeignKey(default=disasterinfosite.models.Volcano_Lahar_kingco.getGroup, to='disasterinfosite.ShapefileGroup')),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Liquefact_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_Liquefact_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Nisqual68_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_Nisqual68_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_SeattleFault72_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_SeattleFault72_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Tsunami_SeaFault72_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_Tsunami_SeaFault72_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_URM_DensityZones_seattle_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.EQ_URM_DensityZones_seattle', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_WUI_kingco_only_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Fire_WUI_kingco_only', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_100yr_wUrban_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_100yr_wUrban_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_500yr_wUrban_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_500yr_wUrban_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_CMZ_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_CMZ_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_DamInundation_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_DamInundation', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_nearest_sand_distr_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Flood_nearest_sand_distr', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Hubs_Nearest_seattle_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Hubs_Nearest_seattle', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_ExistingAreas_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.LSLD_ExistingAreas_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='LSLD_Prone_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.LSLD_Prone_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Volcano_Lahar_kingco_filter',
            field=models.ForeignKey(null=True, to='disasterinfosite.Volcano_Lahar_kingco', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True),
        ),
    ]
