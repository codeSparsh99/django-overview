# Generated by Django 4.2.1 on 2023-05-30 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('role', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserCustom',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('fullname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='UserRole',
            fields=[
                ('id', models.UUIDField(primary_key=True, serialize=False)),
                ('role_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.role')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rest_api.usercustom')),
            ],
        ),
    ]