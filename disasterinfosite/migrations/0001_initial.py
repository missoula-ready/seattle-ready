# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import embed_video.fields
import django.db.models.deletion
import django.contrib.gis.db.models.fields

from disasterinfosite.models import OverwriteStorage

class Migration(migrations.Migration):
    operations = [
            migrations.CreateModel(
            name='SiteSettings',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('about_text', models.TextField(help_text='Describe the data and the agencies that it came from.', default='Information about your organization goes here.')),
                ('contact_email', models.EmailField(blank=True, help_text='Put a contact email for the maintainer of this site here.', max_length=254)),
                ('site_url', models.URLField(default='https://www.example.com', help_text='Put the URL to this site here.')),
                ('site_title', models.CharField(default='Your Title Here!', max_length=50)),
                ('site_description', models.CharField(default='A disaster preparedness website', help_text='A small, catchy description for this site.', max_length=200)),
                ('data_download', models.URLField(help_text='A link where people can download a zipfile of all the data that powers this site.', blank=True)),
                ('intro_text', models.TextField(help_text='A description of what we are trying to help people prepare for, or the goal of your site.', default='A natural disaster could strike your area at any time.')),
                ('who_made_this', models.TextField(help_text='Include information about who you are and how to contact you.', default='Information about the creators and maintainers of this particular site.'))
            ],
            options={
                'verbose_name': 'Site Settings',
            },
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('area_name', models.CharField(default='the affected area', help_text="Describe the entire area that this app covers, e.g. 'Oregon' or 'Missoula County'.", max_length=100)),
                ('community_leaders', models.TextField(help_text='Information about community leaders, how to contact them, and form groups.', default='Information about community leaders goes here.')),
            ],
            options={
                'verbose_name': 'Location Information'
            },
        ),
        migrations.CreateModel(
            name='SupplyKit',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('days', models.PositiveIntegerField(help_text="The number of days' worth of supplies prepared residents should have on hand.", default=3)),
                ('text', models.TextField(help_text='More information about building your supply kit. Any web address in here gets turned into a link automatically.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ImportantLink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(max_length=50, help_text="A title for your important link, like 'Evacuation Information'")),
                ('link', models.TextField(help_text='Your link and any information about it. Any web address in here gets turned into a link automatically.')),
            ],
        ),
        migrations.CreateModel(
            name='RecoveryLevels',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('shortLabel', models.CharField(max_length=2)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Infrastructure',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('eventOccursRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('firstDayRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('threeDaysRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('sevenDaysRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('fourWeeksRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('threeMonthsRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('sixMonthsRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('twelveMonthsRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('threeYearsRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('threePlusYearsRecovery', models.ForeignKey(to='disasterinfosite.RecoveryLevels', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),

            ],
        ),
        migrations.CreateModel(
            name='InfrastructureGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('items', models.ManyToManyField(to='disasterinfosite.Infrastructure')),
            ],
        ),
        migrations.CreateModel(
            name='InfrastructureCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('groups', models.ManyToManyField(to='disasterinfosite.InfrastructureGroup'))
            ],
        ),
        migrations.CreateModel(
            name='ShapefileGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('name', models.CharField(max_length=50)),
                ('display_name', models.CharField(max_length=50)),
                ('order_of_appearance', models.IntegerField(help_text='The order, from left to right, in which you would like this group to appear, when applicable.', default=0)),
                ('likely_scenario_title', models.CharField(max_length=80, blank=True)),
                ('likely_scenario_text', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetType',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('model_name', models.CharField(choices=[('SNUG_TEXT', 'TextSnugget')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SnuggetSection',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('order_of_appearance', models.IntegerField(default=0, help_text="The order in which you'd like this to appear in the tab. 0 is at the top."))
            ],
        ),
        migrations.CreateModel(
            name='SnuggetSubSection',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('order_of_appearance', models.IntegerField(default=0, help_text="The order in which you'd like this to appear in the section. 0 is at the top. These can be in different sections or mutually exclusive, hence the non-unique values."))
            ],
        ),
        migrations.CreateModel(
            name='Snugget',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', auto_created=True, serialize=False)),
                ('section', models.ForeignKey(to='disasterinfosite.SnuggetSection', on_delete=django.db.models.deletion.PROTECT, related_name='+')),
                ('sub_section', models.ForeignKey(to='disasterinfosite.SnuggetSubSection', on_delete=django.db.models.deletion.PROTECT, related_name='+', blank=True, null=True)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', null=True, on_delete=django.db.models.deletion.PROTECT))

            ],
        ),
        migrations.CreateModel(
            name='TextSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, to='disasterinfosite.Snugget', serialize=False, primary_key=True, parent_link=True)),
                ('content', models.TextField()),
                ('image', models.TextField(default="")),
                ('percentage', models.FloatField(null=True)),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='EmbedSnugget',
            fields=[
                ('snugget_ptr', models.OneToOneField(auto_created=True, to='disasterinfosite.Snugget', serialize=False, primary_key=True, parent_link=True)),
                ('embed', embed_video.fields.EmbedVideoField()),
            ],
            bases=('disasterinfosite.snugget',),
        ),
        migrations.CreateModel(
            name='PastEventsPhoto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('group', models.ForeignKey(to='disasterinfosite.ShapefileGroup', null=True, on_delete=django.db.models.deletion.PROTECT)),
                ('image', models.ImageField(upload_to='photos')),
                ('caption', models.TextField(default="", max_length=500))
            ],
        ),
         migrations.CreateModel(
            name='DataOverviewImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('link_text', models.CharField(max_length=100, default='')),
                ('image', models.ImageField(storage=OverwriteStorage(), upload_to='data')),
            ],
        ),
         migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('address1', models.CharField(max_length=200, blank=True)),
                ('address2', models.CharField(max_length=200, blank=True)),
                ('city', models.CharField(max_length=200, blank=True)),
                ('state', models.CharField(max_length=50, blank=True)),
                ('zip_code', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]
