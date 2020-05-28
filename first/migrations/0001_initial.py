# Generated by Django 3.0.3 on 2020-05-28 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('nfc', models.CharField(max_length=1000)),
                ('type_id', models.IntegerField()),
                ('act_name', models.CharField(max_length=1000)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_Activity',
            },
        ),
        migrations.CreateModel(
            name='ActivityType',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('act_type', models.CharField(max_length=32, unique=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_ActivityType',
            },
        ),
        migrations.CreateModel(
            name='ActSta',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('act_id', models.IntegerField()),
                ('start_time', models.IntegerField()),
                ('end_time', models.IntegerField()),
                ('moment_text', models.CharField(default='', max_length=1000)),
                ('is_shared', models.IntegerField(default=0)),
                ('shared_time', models.DateTimeField(auto_now=True)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_ActSta',
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('from_id', models.IntegerField()),
                ('to_id', models.IntegerField()),
                ('content', models.CharField(max_length=1000)),
                ('is_processed', models.IntegerField(default=0)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_Application',
            },
        ),
        migrations.CreateModel(
            name='Box',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('nfc', models.CharField(max_length=1000)),
                ('box_name', models.CharField(max_length=1000)),
                ('box_pos', models.CharField(max_length=1000)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_Box',
            },
        ),
        migrations.CreateModel(
            name='BoxContent',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('box_id', models.IntegerField()),
                ('thing_name', models.CharField(max_length=1000)),
                ('thing_num', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_BoxContent',
            },
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_id', models.IntegerField()),
                ('friend_id', models.IntegerField()),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_Friend',
            },
        ),
        migrations.CreateModel(
            name='PushNote',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('author_id', models.IntegerField()),
                ('title', models.CharField(max_length=1000)),
                ('summary', models.CharField(max_length=1000)),
                ('contents', models.CharField(max_length=10000)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_PushNote',
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('nid', models.AutoField(primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=32, unique=True)),
                ('password', models.CharField(max_length=32)),
                ('active_day', models.IntegerField(default=0)),
                ('last_act', models.CharField(default='1970-01-01', max_length=1000)),
                ('created_time', models.DateTimeField(auto_now=True)),
                ('updated_time', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'guan_UserInfo',
            },
        ),
    ]
