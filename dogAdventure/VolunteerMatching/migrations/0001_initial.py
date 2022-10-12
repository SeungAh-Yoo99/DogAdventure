# Generated by Django 4.1.2 on 2022-10-12 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbandonedDog',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=64)),
                ('gender', models.CharField(max_length=8)),
                ('airport', models.CharField(max_length=64)),
                ('time_agreement', models.BooleanField(default=False)),
                ('datetime', models.DateTimeField()),
                ('weight', models.IntegerField()),
                ('info', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='VolunteerMatching.abandoneddog')),
            ],
        ),
    ]
