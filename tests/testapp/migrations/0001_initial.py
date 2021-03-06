# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-01 06:28
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_fsm
import testapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50, protected=True)),
            ],
            options={
                'permissions': [('can_publish_post', 'Can publish post'), ('can_remove_post', 'Can remove post')],
            },
        ),
        migrations.CreateModel(
            name='BlogPostWithCustomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlogPostWithStringField',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='DbState',
            fields=[
                ('id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('label', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ExceptionalBlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='FKApplication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMKeyField(default=b'new', on_delete=django.db.models.deletion.PROTECT, to='testapp.DbState')),
            ],
        ),
        migrations.CreateModel(
            name='Insect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(choices=[(b'CTR', b'Caterpillar'), (b'BTF', b'Butterfly')], default=b'CTR', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='LockedBlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50, protected=True)),
                ('text', models.CharField(max_length=50)),
            ],
            bases=(django_fsm.ConcurrentTransitionMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MixinSupportTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
            bases=(testapp.models.WorkflowMixin, models.Model),
        ),
        migrations.CreateModel(
            name='MultiResultTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ObjectPermissionTestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
            options={
                'permissions': [('can_publish_objectpermissiontestmodel', 'Can publish ObjectPermissionTestModel')],
            },
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='contenttypes.ContentType')),
            ],
        ),
        migrations.CreateModel(
            name='TestExceptTargetTransitionShortcut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', django_fsm.FSMField(default=b'new', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('signal_counter', models.IntegerField(default=0)),
                ('state', django_fsm.FSMField(default=b'SUBMITTED_BY_USER', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='ExtendedBlogPost',
            fields=[
                ('lockedblogpost_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='testapp.LockedBlogPost')),
                ('review_state', django_fsm.FSMField(default=b'waiting', max_length=50, protected=True)),
                ('notes', models.CharField(max_length=50)),
            ],
            bases=('testapp.lockedblogpost',),
        ),
        migrations.CreateModel(
            name='Butterfly',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('testapp.insect',),
        ),
        migrations.CreateModel(
            name='Caterpillar',
            fields=[
            ],
            options={
                'indexes': [],
                'proxy': True,
            },
            bases=('testapp.insect',),
        ),
    ]
